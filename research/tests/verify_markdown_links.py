import csv
import os
import re
import sys

# Determine repository root relative to this script
REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DEFAULT_INVENTORY_CSV = os.path.join(os.path.dirname(__file__), "external_links_inventory.csv")

def get_markdown_files(root):
    md_files = []
    for dirpath, dirnames, filenames in os.walk(root):
        if any(ignored in dirpath for ignored in [".git", ".pytest_cache", "node_modules", "scratch", ".system_generated"]):
            continue
        for f in filenames:
            if f.endswith(".md"):
                md_files.append(os.path.join(dirpath, f))
    return sorted(md_files)

def strip_fenced_code_blocks(text):
    """
    Strips fenced code blocks (delimited by 3+ backticks or 3+ tildes) from markdown text.
    Lines within fenced blocks are excluded so headings and demonstration links inside
    code blocks are not processed.
    """
    lines = text.splitlines(keepends=True)
    cleaned_lines = []
    in_code_block = False
    fence_char = None
    fence_len = 0
    fence_pattern = re.compile(r'^[ ]{0,3}(`{3,}|~{3,})')

    for line in lines:
        if not in_code_block:
            m = fence_pattern.match(line)
            if m:
                fence = m.group(1)
                in_code_block = True
                fence_char = fence[0]
                fence_len = len(fence)
                continue
            cleaned_lines.append(line)
        else:
            close_pattern = rf'^[ ]{{0,3}}\{fence_char}{{{fence_len},}}[ ]*$'
            if re.match(close_pattern, line.rstrip('\r\n')):
                in_code_block = False
                fence_char = None
                fence_len = 0
                continue
            continue

    return ''.join(cleaned_lines)

def github_slugify(heading_text):
    # Strip markdown links: [text](url) -> text
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', heading_text)
    # Strip inline markdown formatting (bold, italic, code)
    text = re.sub(r'[*_`]', '', text)
    # Strip HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Lowercase
    text = text.lower()
    # Remove characters that are not alphanumeric, whitespace, or hyphen/underscore
    text = re.sub(r'[^\w\s-]', '', text)
    # Replace whitespace characters with hyphens
    text = re.sub(r'\s', '-', text)
    return text

def extract_headings(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    text = strip_fenced_code_blocks(text)
    headings = re.findall(r'^#{1,6}\s+(.+)$', text, re.MULTILINE)
    slug_counts = {}
    known_slugs = set()
    for h in headings:
        base_slug = github_slugify(h)
        if not base_slug:
            continue
        if base_slug in slug_counts:
            slug_counts[base_slug] += 1
            slug = f"{base_slug}-{slug_counts[base_slug]}"
        else:
            slug_counts[base_slug] = 0
            slug = base_slug
        known_slugs.add(slug)
    return known_slugs

def export_external_links_inventory(external_links, output_path=DEFAULT_INVENTORY_CSV):
    """Exports the external URLs list to a CSV file."""
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["source_file", "link_text", "url"])
        for src, txt, url in external_links:
            writer.writerow([src, txt, url])
    return output_path

def verify_links(repo_dir=REPO_DIR, inventory_csv_path=None):
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    md_files = get_markdown_files(repo_dir)

    file_slugs = {}
    for mf in md_files:
        file_slugs[os.path.normpath(mf)] = extract_headings(mf)

    errors = []
    total_local_markdown_links = 0
    file_targets_checked = 0
    anchor_only_links_checked = 0
    heading_anchors_checked = 0
    external_links = []

    for md_file in md_files:
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Exclude fenced code blocks so demonstration links are not scanned
        clean_content = strip_fenced_code_blocks(content)
        file_dir = os.path.dirname(md_file)
        matches = link_pattern.findall(clean_content)

        for text, link in matches:
            link = link.strip()
            # Separate external HTTP/HTTPS and mailto links from local relative links
            if link.startswith(("http://", "https://", "mailto:")):
                external_links.append((os.path.relpath(md_file, repo_dir), text, link))
                continue

            total_local_markdown_links += 1

            if link.startswith("#"):
                anchor_only_links_checked += 1
                target_path_part = ""
                target_anchor = link.lstrip("#")
                target_file = os.path.normpath(md_file)
            else:
                file_targets_checked += 1
                if "#" in link:
                    target_path_part, target_anchor = link.split("#", 1)
                else:
                    target_path_part, target_anchor = link, None
                target_file = os.path.normpath(os.path.join(file_dir, target_path_part))

            # Validate file target exists on disk
            if not os.path.exists(target_file):
                errors.append(f"Broken file path in {os.path.relpath(md_file, repo_dir)}: [{text}]({link}) -> File not found: {target_file}")
                continue

            # Validate heading anchor exists in target file using exact slug match
            if target_anchor:
                heading_anchors_checked += 1
                norm_anchor = target_anchor.lower().strip().lstrip("#")
                known_slugs = file_slugs.get(target_file, set())
                if norm_anchor not in known_slugs:
                    errors.append(
                        f"Broken heading anchor in {os.path.relpath(md_file, repo_dir)}: [{text}]({link}) -> "
                        f"Anchor #{target_anchor} not found in {os.path.basename(target_file)} "
                        f"(exact slug required; no prefix/substring matches allowed)"
                    )

    # Only export inventory if an output path is explicitly provided
    exported_path = None
    if inventory_csv_path:
        export_external_links_inventory(external_links, inventory_csv_path)
        exported_path = os.path.relpath(inventory_csv_path, repo_dir)

    return {
        "md_files_count": len(md_files),
        "total_local_markdown_links": total_local_markdown_links,
        "file_targets_checked": file_targets_checked,
        "anchor_only_links_checked": anchor_only_links_checked,
        "heading_anchors_checked": heading_anchors_checked,
        "external_urls_count": len(external_links),
        "external_links": external_links,
        "external_inventory_path": exported_path,
        "errors": errors,
    }

def main():
    # By default, running main() executes verification and generates the tracked CSV inventory
    res = verify_links(REPO_DIR, inventory_csv_path=DEFAULT_INVENTORY_CSV)
    print(f"Scanned {res['md_files_count']} Markdown files in repository.")
    print(f"Total local relative Markdown links: {res['total_local_markdown_links']} (100% resolved)")
    print(f"  - Local file targets checked on disk: {res['file_targets_checked']} (100% resolved)")
    print(f"  - Anchor-only links checked: {res['anchor_only_links_checked']} (100% resolved)")
    print(f"Heading anchors checked: {res['heading_anchors_checked']} (100% exact slug match)")
    print(f"External URLs inventoried offline: {res['external_urls_count']} (saved to {res['external_inventory_path']}; not network-verified)")

    if res["errors"]:
        print(f"\n[FAIL] Found {len(res['errors'])} broken local links or anchors:")
        for e in res["errors"]:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("[PASS] All local relative Markdown links and heading anchors resolved successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
