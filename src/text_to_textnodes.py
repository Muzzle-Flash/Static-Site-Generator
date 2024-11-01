from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_urls import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


def text_to_textnodes(text):
    node = TextNode(text, TextType.NORMAL)
    nodes = [node]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    return nodes