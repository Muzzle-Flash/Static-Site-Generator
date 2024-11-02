from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from text_to_textnodes import text_to_textnodes
from textnode_to_html import text_node_to_html_node
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

def markdown_to_html_node(markdown):
    def text_to_children(text):
        nodes = text_to_textnodes(text)
        result = []
        for node in nodes:
            result.append(text_node_to_html_node(node))
        return result


    blocks = markdown_to_blocks(markdown)
    parent_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case 'paragraph':
                children = text_to_children(block)
                node =  ParentNode(children, 'p')
                parent_nodes.append(node)
            case 'heading':
                hash_num = 0
                for letter in block:
                    if letter == '#':
                        hash_num += 1
                    if letter != '#':
                        break
                content = block[hash_num:].lstrip()
                children = text_to_children(content)
                node =  ParentNode(children, f'h{hash_num}')
                parent_nodes.append(node)
            case 'code':
                content = block[3:-3]
                children = text_to_children(content)
                code_node =  ParentNode(children, f'code')
                node = ParentNode([code_node], 'pre')
                parent_nodes.append(node)
            case 'quote':
                cleaned_lines = [line.strip('>') for line in block.split("\n")]
                cleaned_lines = [line.strip() for line in cleaned_lines]
                content = "\n".join(cleaned_lines)
                children = text_to_children(content)
                node =  ParentNode(children, f'blockquote')
                parent_nodes.append(node)
            case 'unordered_list':
                lines = []
                for line in block.split("\n"):
                    lines.append(line[1:])
                children = []
                for line in lines:
                    line = line.strip()
                    item_node = ParentNode(text_to_children(line), 'li')
                    children.append(item_node)
                node = ParentNode(children, 'ul')
                parent_nodes.append(node)
            case 'ordered_list':
                lines = []
                for line in block.split("\n"):
                    lines.append(line[2:])
                children = []
                for line in lines:
                    line = line.strip()
                    item_node = ParentNode(text_to_children(line), 'li')
                    children.append(item_node)
                node = ParentNode(children, 'ol')
                parent_nodes.append(node)
    grandparent_node = ParentNode(parent_nodes, 'div')
    return grandparent_node