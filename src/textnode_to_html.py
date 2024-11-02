from leafnode import LeafNode
from textnode import TextType

def text_node_to_html_node(text_node):
    if not text_node.text:
        raise ValueError("LeafNode must have a Value")
    
    match text_node.text_type:
        case TextType.NORMAL:
            node = LeafNode(text_node.text)
            return node
        case TextType.BOLD:
            node = LeafNode(text_node.text, None, "b")
            return node
        case TextType.ITALIC:
            node = LeafNode(text_node.text, None, "i")
            return node
        case TextType.CODE:
            node = LeafNode(text_node.text, None, "code")
            return node
        case TextType.LINK:
            node = LeafNode(text_node.text, {"href": text_node.url}, "a")
            return node
        case TextType.IMAGE:
            node = LeafNode("", {"src": text_node.url, "alt": text_node.text}, "img")
            #node = LeafNode("", {"src": text_node.url, "alt": text_node.text}, "img")
            return node
        case _:
            print("oops")
            raise Exception("Invalid type")