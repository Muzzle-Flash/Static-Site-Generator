import unittest
from textnode import TextNode, TextType
from leafnode import LeafNode
from texttohtml import text_node_to_html_node

class TestTextToHTML(unittest.TestCase):
    def test_no_text(self):
        node = TextNode(None, "bold", None)
        with self.assertRaises(ValueError) as context:
            text_node_to_html_node(node)
        self.assertEqual(str(context.exception), "LeafNode must have a Value")

    def test_no_type(self):
        node = TextNode("I'm tired", None, None)
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(node)
        self.assertEqual(str(context.exception), "Invalid type")

    def test_invalid_type(self):
        node = TextNode("so tired", "ARABIC", None)
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(node)
        self.assertEqual(str(context.exception), "Invalid type")

    def test_no_url(self):
        node = TextNode("Everything at once", "link", None)
        expected_result = "HTMLNode(a, Everything at once, None, {'href': None})"
        self.assertEqual(repr(text_node_to_html_node(node)), expected_result)
        
        

if __name__ == "__main__":
    unittest.main()