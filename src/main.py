from textnode import *
from texttohtml import text_node_to_html_node
from split_nodes_delimiter import split_nodes_delimiter
def main():
    node = TextNode("This is text with a `code block` word", TextType.NORMAL)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    print(new_nodes)
if __name__=="__main__":
    main()