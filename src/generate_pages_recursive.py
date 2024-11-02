from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node
import os

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    def recursive_BS(current_source_path, current_dest_path):
        for item in os.listdir(current_source_path):
            source_item_path = os.path.join(current_source_path, item)
            dest_file_path = os.path.join(current_dest_path, item)
            print(dest_file_path)
            if os.path.isdir(source_item_path):
                if not os.path.exists(dest_file_path):
                    os.mkdir(os.path.join(current_dest_path, item))
                recursive_BS(source_item_path, dest_file_path)
            if os.path.isfile(source_item_path):
                dest_file_path = os.path.join(current_dest_path, item.replace('.md', '.html'))
                print(f'file {item}')
                with open(source_item_path) as file:
                    markdown = file.read()
                with open(template_path) as file:
                    template = file.read()
                title = extract_title(markdown)
                HTML_string = markdown_to_html_node(markdown).to_html()
                HTML_file = template.replace('{{ Title }}', title)
                HTML_file = HTML_file.replace('{{ Content }}', HTML_string)
                if not os.path.exists(dest_file_path):
                    with open(dest_file_path, 'w') as file:
                        file.write(HTML_file)
    
    
    
    
    recursive_BS(dir_path_content, dest_dir_path)