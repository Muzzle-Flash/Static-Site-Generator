from textnode import TextType, TextNode
from extract_from_markdown import extract_markdown_links, extract_markdown_images

def process_text(text, extractor, text_type):
    result = []
    while text:
        items = extractor(text)
        if not items:
            result.append(TextNode(text, TextType.NORMAL))
            break
        descriptor, url = items[0]
        match text_type:
            case TextType.IMAGE:
                markdown_string = f"![{descriptor}]({url})"
            case TextType.LINK:
                markdown_string = f"[{descriptor}]({url})"
        before, markdown, after = text.partition(markdown_string)

        if before:
            result.append(TextNode(before, TextType.NORMAL))

        result.append(TextNode(descriptor, text_type, url))
        text = after

    return result

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text == '':
            raise ValueError("TextNode Text cannot be empty")
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
        else:
            new_nodes.extend(process_text(node.text, extract_markdown_images, TextType.IMAGE))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text == '':
            raise ValueError("TextNode Text cannot be empty")
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
        else:
            new_nodes.extend(process_text(node.text, extract_markdown_links, TextType.LINK))
    return new_nodes