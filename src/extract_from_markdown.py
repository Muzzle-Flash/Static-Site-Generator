import re

def extract_markdown_images(text):
    regex = r'!\[([^\[\]]*)\]\(([^\(\)]*)\)'
    keywords = re.findall(regex, text)
    return keywords

def extract_markdown_links(text):
    regex = r'[^!]\[([^\[\]]*)\]\(([^\[\]]*)\)'
    keywords = re.findall(regex, text)
    return keywords