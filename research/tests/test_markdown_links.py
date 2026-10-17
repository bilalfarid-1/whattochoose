import os
import tempfile
import pytest
from research.tests.verify_markdown_links import (
    github_slugify,
    extract_headings,
    verify_links,
    REPO_DIR,
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
    
    res = verify_links(str(tmp_path))
    assert res["external_urls_count"] == 1
    assert res["total_local_markdown_links"] == 2
    assert res["file_targets_checked"] == 1
    assert res["anchor_only_links_checked"] == 1
    assert res["heading_anchors_checked"] == 1
    assert len(res["errors"]) == 0

def test_repository_markdown_links_clean():
    """Verify that the actual repository passes 100% with zero broken links or anchors."""
    res = verify_links(REPO_DIR)
    assert len(res["errors"]) == 0, f"Found broken links in repo: {res['errors']}"
    assert res["total_local_markdown_links"] == 69
    assert res["file_targets_checked"] == 68
    assert res["anchor_only_links_checked"] == 1
    assert res["heading_anchors_checked"] == 1
    assert res["external_urls_count"] == 114
    assert os.path.exists(os.path.join(REPO_DIR, res["external_inventory_path"]))
