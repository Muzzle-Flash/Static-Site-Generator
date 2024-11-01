from textnode import *
from text_to_html import text_node_to_html_node
from split_nodes_delimiter import split_nodes_delimiter
from text_to_textnodes import text_to_textnodes
from markdown_to_blocks import markdown_to_blocks
def main():
    test_md = """
        # This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item
        """

    result = markdown_to_blocks(test_md)
    for block in result:
        print(f"block: '{block}'")


if __name__=="__main__":
    main()