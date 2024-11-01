from leafnode import LeafNode
from textnode import TextType

def text_node_to_html_node(text_node):
    if not text_node.text:
        raise ValueError("LeafNode must have a Value")
    
    match text_node.text_type:
        case "normal":
            node = LeafNode(text_node.text)
            return node
        case "bold":
            node = LeafNode(text_node.text, None, "b")
            return node
        case "italic":
            node = LeafNode(text_node.text, None, "i")
            return node
        case "code":
            node = LeafNode(text_node.text, None, "code")
            return node
        case "link":
            node = LeafNode(text_node.text, {"href": text_node.url}, "a")
            return node
        case "image":
            node = LeafNode("", {"src": text_node.url, "alt": text_node.text}, "img")
        case _:
            print("oops")
            raise Exception("Invalid type")