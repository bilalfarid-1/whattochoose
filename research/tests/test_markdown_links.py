import os
import tempfile
import pytest
from research.tests.verify_markdown_links import (
    github_slugify,
    extract_headings,
    strip_fenced_code_blocks,
    verify_links,
    export_external_links_inventory,
    REPO_DIR,
    DEFAULT_INVENTORY_CSV,
)

def test_github_slugify_standard_and_edge_cases():
    # 1. Standard heading
    assert github_slugify("Four-hour daily routine") == "four-hour-daily-routine"

    # 2. Heading with emoji, colon, and ampersand
    assert github_slugify("🚀 JobPulse: Production Architecture & Key Features") == "-jobpulse-production-architecture--key-features"

    # 3. Heading with code and bold markdown
    assert github_slugify("Heading with `code` and **bold**") == "heading-with-code-and-bold"

    # 4. Heading with link inside
    assert github_slugify("Heading with [link](https://example.com) inside") == "heading-with-link-inside"

    # 5. HTML tags inside heading
    assert github_slugify("Heading with <span>HTML</span>") == "heading-with-html"

def test_strip_fenced_code_blocks_backticks_and_tildes():
    doc = """# Real Title

```python
# Fake Heading In 3 Backticks
[Broken Link In Code](fake_path_1.md)
```

````markdown
# Fake Heading In 4 Backticks
[Broken Link In 4 Backticks](fake_path_2.md)
````

~~~bash
## Fake Heading In Tildes
[Broken Link In Tildes](fake_path_3.md)
~~~

[Valid Link](target.md)
"""
    cleaned = strip_fenced_code_blocks(doc)
    assert "# Real Title" in cleaned
    assert "[Valid Link](target.md)" in cleaned
    assert "fake_path_1.md" not in cleaned
    assert "fake_path_2.md" not in cleaned
    assert "fake_path_3.md" not in cleaned
    assert "Fake Heading" not in cleaned

def test_fenced_code_blocks_ignored_in_heading_and_link_extraction(tmp_path):
    """
    Demonstrates that:
    1. Headings inside backtick-fenced and tilde-fenced code blocks are NOT extracted as valid anchors.
    2. Demonstration links inside backtick-fenced and tilde-fenced blocks do NOT produce false broken-link errors.
    3. A link attempting to target a heading that appears only inside code blocks FAILS.
    """
    code_examples_md = tmp_path / "examples.md"
    code_examples_md.write_text("""# Real Section

```markdown
# Fake Heading In Backticks
[Demonstration Broken Link](missing_file_in_backticks.md)
```

~~~text
## Fake Heading In Tildes
[Another Broken Demo Link](missing_file_in_tildes.md)
~~~

[Real Link To Self](#real-section)
""", encoding="utf-8")

    caller_md = tmp_path / "caller.md"
    caller_md.write_text("""[Link To Fake Backtick Heading](examples.md#fake-heading-in-backticks)
[Link To Fake Tilde Heading](examples.md#fake-heading-in-tildes)
[Link To Real Section](examples.md#real-section)
""", encoding="utf-8")

    res = verify_links(str(tmp_path))

    # The two demonstration links inside fenced code blocks must NOT be reported as broken file errors
    broken_file_errors = [e for e in res["errors"] if "missing_file" in e]
    assert len(broken_file_errors) == 0, f"Expected 0 false errors from code blocks, got: {broken_file_errors}"

    # Links attempting to target headings that only exist inside code blocks must FAIL
    anchor_errors = [e for e in res["errors"] if "fake-heading" in e]
    assert len(anchor_errors) == 2, f"Expected 2 anchor errors for fake code headings, got: {anchor_errors}"

    # Verify total heading anchors checked (1 anchor-only in examples.md + 3 cross-file in caller.md)
    assert res["heading_anchors_checked"] == 4

def test_extract_headings_duplicate_disambiguation(tmp_path):
    md_content = """# Overview
## Features
## Features
## Features
### Overview
"""
    test_file = tmp_path / "test_doc.md"
    test_file.write_text(md_content, encoding="utf-8")

    slugs = extract_headings(str(test_file))

    # First occurrence is base slug
    assert "overview" in slugs
    assert "features" in slugs
    # Subsequent duplicates are disambiguated with -1, -2
    assert "features-1" in slugs
    assert "features-2" in slugs
    assert "overview-1" in slugs

def test_anchor_validation_exact_pass_and_broken_prefix_fail(tmp_path):
    """
    Demonstrates that:
    1. Valid exact GitHub slug anchors PASS.
    2. Broken-prefix anchors (e.g. #-jobpulse-production-architecture) FAIL because
       substring fallback matching was eliminated.
    """
    target_md = tmp_path / "target.md"
    target_md.write_text("## 🚀 JobPulse: Production Architecture & Key Features\n\nContent here.\n", encoding="utf-8")

    # 1. Exact valid anchor in caller
    caller_valid = tmp_path / "caller_valid.md"
    caller_valid.write_text("[Valid Link](target.md#-jobpulse-production-architecture--key-features)\n", encoding="utf-8")
    res_valid = verify_links(str(tmp_path))
    assert len(res_valid["errors"]) == 0
    assert res_valid["heading_anchors_checked"] == 1

    # 2. Broken-prefix anchor in caller (missing suffix)
    caller_broken_prefix = tmp_path / "caller_broken.md"
    caller_broken_prefix.write_text("[Broken Prefix](target.md#-jobpulse-production-architecture)\n", encoding="utf-8")
    res_broken = verify_links(str(tmp_path))
    assert len(res_broken["errors"]) == 1
    assert "exact slug required; no prefix/substring matches allowed" in res_broken["errors"][0]

def test_anchor_validation_anchor_only_links(tmp_path):
    doc = tmp_path / "doc.md"
    doc.write_text("""# Introduction
[Jump to section](#section-two)
[Jump to broken](#section)

## Section Two
Content.
""", encoding="utf-8")

    res = verify_links(str(tmp_path))
    assert res["anchor_only_links_checked"] == 2
    assert res["file_targets_checked"] == 0
    # One valid, one broken prefix (#section vs #section-two)
    assert len(res["errors"]) == 1
    assert "Anchor #section not found" in res["errors"][0]

def test_external_links_inventory_and_counts(tmp_path):
    doc = tmp_path / "links.md"
    doc.write_text("""[Google](https://google.com)
[Local File](target.md)
[Same File Anchor](#section)

# Section
""", encoding="utf-8")
    (tmp_path / "target.md").write_text("# Target\n", encoding="utf-8")

    custom_csv = tmp_path / "custom_inventory.csv"
    res = verify_links(str(tmp_path), inventory_csv_path=str(custom_csv))
    assert res["external_urls_count"] == 1
    assert res["total_local_markdown_links"] == 2
    assert res["file_targets_checked"] == 1
    assert res["anchor_only_links_checked"] == 1
    assert res["heading_anchors_checked"] == 1
    assert len(res["errors"]) == 0
    assert custom_csv.exists()
    assert "https://google.com" in custom_csv.read_text(encoding="utf-8")

def test_tmp_path_does_not_modify_tracked_csv(tmp_path):
    """
    Regression test ensuring that test runs using tmp_path NEVER overwrite
    or modify the repository's tracked external_links_inventory.csv.
    """
    assert os.path.exists(DEFAULT_INVENTORY_CSV), "Tracked external_links_inventory.csv must exist"
    with open(DEFAULT_INVENTORY_CSV, "r", encoding="utf-8") as f:
        original_content = f.read()
    original_mtime = os.path.getmtime(DEFAULT_INVENTORY_CSV)

    # Run verification against a tmp_path with dummy links
    dummy_doc = tmp_path / "dummy.md"
    dummy_doc.write_text("[Dummy Link](https://dummy-url-for-test.example.com)\n", encoding="utf-8")

    # 1. verify_links without inventory_csv_path
    res_no_export = verify_links(str(tmp_path))
    assert res_no_export["external_urls_count"] == 1

    # 2. verify_links with an isolated tmp_path CSV
    isolated_csv = tmp_path / "isolated.csv"
    res_isolated = verify_links(str(tmp_path), inventory_csv_path=str(isolated_csv))
    assert isolated_csv.exists()
    assert "https://dummy-url-for-test.example.com" in isolated_csv.read_text(encoding="utf-8")

    # Verify tracked CSV was strictly unmodified
    with open(DEFAULT_INVENTORY_CSV, "r", encoding="utf-8") as f:
        current_content = f.read()
    current_mtime = os.path.getmtime(DEFAULT_INVENTORY_CSV)

    assert current_content == original_content, "Tracked CSV content was mutated by tmp_path test!"
    assert current_mtime == original_mtime, "Tracked CSV mtime was modified by tmp_path test!"

def test_repository_markdown_links_clean():
    """Verify that the actual repository passes 100% with zero broken links or anchors."""
    res = verify_links(REPO_DIR)
    assert len(res["errors"]) == 0, f"Found broken links in repo: {res['errors']}"
    assert res["total_local_markdown_links"] == 161
    assert res["file_targets_checked"] == 160
    assert res["anchor_only_links_checked"] == 1
    assert res["heading_anchors_checked"] == 1
    assert res["external_urls_count"] == 125

