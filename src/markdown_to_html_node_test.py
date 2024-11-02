import unittest
from parentnode import ParentNode
from leafnode import LeafNode
from htmlnode import HTMLNode
from markdown_to_html_node import markdown_to_html_node

class test_markdown_to_html(unittest.TestCase):
    def test_heading_conversion(self):
        markdown = "## Heading"
        node = markdown_to_html_node(markdown)
        self.assertIsInstance(node, ParentNode)
        self.assertEqual(node.tag, 'div')
        child = node.children[0]
        self.assertEqual(child.tag, 'h2')

    def test_heading_content(self):
        markdown = "## Heading"
        node = markdown_to_html_node(markdown)
        expected = HTMLNode('div', None, [
            HTMLNode('h2', 'Heading')
        ])
        self.assertEqual(node, expected)

    def test_paragraph_conversion(self):
        markdown = "This is a paragraph."
        node = markdown_to_html_node(markdown)
        self.assertIsInstance(node, ParentNode)
        self.assertEqual(node.tag, 'div')
        child = node.children[0]
        self.assertEqual(child.tag, 'p')
    
    def test_paragraph_content(self):
        markdown = "This is a paragraph."
        node = markdown_to_html_node(markdown)
        expected = HTMLNode('div', None, [
            HTMLNode('p', 'This is a paragraph.')
        ])
        self.assertEqual(node, expected)

    def test_code_block_conversion(self):
        markdown = "```code block```"
        node = markdown_to_html_node(markdown)
        self.assertIsInstance(node, ParentNode)
        self.assertEqual(node.tag, 'div')
        child = node.children[0]
        self.assertEqual(child.tag, 'pre')

    def test_code_block_content(self):
        markdown = "```code block```"
        node = markdown_to_html_node(markdown)
        expected = HTMLNode('div', None, [
            HTMLNode('code', 'code block')
        ])
        self.assertEqual(node, expected)
    
    def test_quote_conversion(self):
        markdown = """>this is a quotable quote
        >from a quotable movie
        >that I quote every day"""
        node = markdown_to_html_node(markdown)
        self.assertIsInstance(node, ParentNode)
        self.assertEqual(node.tag, 'div')
        child = node.children[0]
        self.assertEqual(child.tag, 'blockquote')

    def test_quote_content(self):
        markdown = """>this is a quotable quote
        >from a quotable movie
        >that I quote every day"""
        node = markdown_to_html_node(markdown)
        expected = HTMLNode('div', None, [
            HTMLNode('blockquote', """this is a quotable quote
        from a quotable movie
        that I quote every day""")
        ])
        self.assertEqual(node, expected)

    def test_unordered_list_conversion(self):
        markdown = """* This is the first list item in a list block
* This is a list item
* This is another list item"""
        node = markdown_to_html_node(markdown)
        self.assertIsInstance(node, ParentNode)
        self.assertEqual(node.tag, 'div')
        child = node.children[0]
        self.assertEqual(child.tag, 'ul')
        grandchild = child.children[0]
        self.assertEqual(grandchild.tag, 'li')

    def test_unordered_list_content(self):
        markdown = """* This is the first list item in a list block
        * This is a list item
        * This is another list item"""
        node = markdown_to_html_node(markdown)
        expected = HTMLNode('div', None, [
            HTMLNode('ul', None, [
                HTMLNode('li', """This is the first list item in a list block
            This is a list item
            This is another list item""")
            ])
        ])
        self.assertEqual(expected, node)

    def test_ordered_list_conversion(self):
        markdown = """1. This is the first list item in a list block
2. This is the second list item
3. This is the third list item
4. This is the fourth list item"""
        node = markdown_to_html_node(markdown)
        self.assertIsInstance(node, ParentNode)
        self.assertEqual(node.tag, 'div')
        child = node.children[0]
        self.assertEqual(child.tag, 'ol')
        grandchild = child.children[0]
        self.assertEqual(grandchild.tag, 'li')

    def test_ordered_list_content(self):
        markdown = """1. This is the first list item in a list block
2. This is the second list item
3. This is the third list item
4. This is the fourth list item"""
        node = markdown_to_html_node(markdown)
        expected = HTMLNode('div', None, [
            HTMLNode('ul', None, [
                HTMLNode('li', """1. This is the first list item in a list block
2. This is the second list item
3. This is the third list item
4. This is the fourth list item""")
            ])
        ])
        self.assertEqual(node, expected)


if __name__ == "__main__":
    unittest.main()