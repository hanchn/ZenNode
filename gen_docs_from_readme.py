import os
import re

README_PATH = "README.md"
FILES_DIR = "files"

def extract_links(readme_path):
    links = []
    with open(readme_path, "r", encoding="utf-8") as f:
        for line in f:
            match = re.search(r"\]\(\./files/(\d{4}\.md)\)", line)
            if match:
                links.append(match.group(1))
    return links

def ensure_files_dir():
    if not os.path.exists(FILES_DIR):
        os.makedirs(FILES_DIR)

def create_md_files(md_files):
    for md_file in md_files:
        file_path = os.path.join(FILES_DIR, md_file)
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"# {md_file.replace('.md', '')}\n\nTODO: 补充文档内容。\n")

def main():
    ensure_files_dir()
    md_files = extract_links(README_PATH)
    create_md_files(md_files)
    print(f"已生成 {len(md_files)} 个文档文件（如有缺失）。")

if __name__ == "__main__":
    main()