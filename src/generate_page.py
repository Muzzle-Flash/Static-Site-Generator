from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node
import os

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    with open(from_path) as file:
        markdown = file.read()
    with open(template_path) as file:
        template = file.read()
    title = extract_title(markdown)
    HTML_string = markdown_to_html_node(markdown).to_html()
    HTML_file = template.replace('{{ Title }}', title)
    HTML_file = HTML_file.replace('{{ Content }}', HTML_string)
    if not os.path.exists(dest_path):
        with open(dest_path, 'w') as file:
            file.write(HTML_file)

