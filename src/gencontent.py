import os
from markdown_blocks import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")


#def extract_title(markdown):
#    for line in markdown.splitlines():
#        if line.strip().startswith('# '):
#            return line.strip()[2:].strip()
#    raise ValueError("No H1 header found in the markdown.")

#def generate_page(from_path, template_path, dest_path):
#    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read markdown content
#    with open(from_path, 'r', encoding='utf-8') as f:
#        markdown_content = f.read()

    # Read template content
#    with open(template_path, 'r', encoding='utf-8') as f:
#        template_content = f.read()
    
    # Convert markdown to HTML
#    html_node = markdown_to_html_node(markdown_content)
#    html_content = html_node.to_html()

    # Extract title
#    title = extract_title(markdown_content)

    # Replace placeholders in template
#    final_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    # Ensure destination directory exists
#    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write final HTML to destination path
#    with open(dest_path, 'w', encoding='utf-8') as f:
#        f.write(final_html)