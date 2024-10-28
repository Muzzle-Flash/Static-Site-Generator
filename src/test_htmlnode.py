import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html1(self):
        node = HTMLNode("a", "http://www.mspaintadventures.com/sweetbroandhellajeff/", None, {"href": "http://www.mspaintadventures.com", "target": "Andrew Hussie"})
        expected_props_to_html = ' href="http://www.mspaintadventures.com" target="Andrew Hussie"'
        self.assertEqual(node.props_to_html(), expected_props_to_html)
    def test_repr(self):
        node = HTMLNode("a", "http://www.mspaintadventures.com/sweetbroandhellajeff/", None, {"href": "http://www.mspaintadventures.com", "target": "Andrew Hussie"})
        expected_repr = "HTMLNode(a, http://www.mspaintadventures.com/sweetbroandhellajeff/, None, {'href': 'http://www.mspaintadventures.com', 'target': 'Andrew Hussie'})"
        self.assertEqual(repr(node), expected_repr)
    def test_empty_node(self):
        node = HTMLNode()
        expected_repr = "HTMLNode(None, None, None, None)"
        self.assertEqual(repr(node), expected_repr)
    def test_node_with_children(self):
        child = HTMLNode("span", "inner text")
        parent = HTMLNode("div", None, [child])
        expected_repr = "HTMLNode(div, None, [HTMLNode(span, inner text, None, None)], None)"
        self.assertEqual(repr(parent), expected_repr)
    def test_tag_and_value(self):
        node = HTMLNode("p", "Hello, world!")
        expected_repr = "HTMLNode(p, Hello, world!, None, None)"
        self.assertEqual(repr(node), expected_repr)
        

if __name__ == "__main__":
    unittest.main()