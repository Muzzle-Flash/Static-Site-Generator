import unittest
from textnode import TextNode, TextType
from split_nodes_urls import *


class TestSplitNodesUrls(unittest.TestCase):
    def test_split_node_image(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.NORMAL)
        expected = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertEqual(split_nodes_image([node]), expected)

    def test_multiple_nodes_image(self):
        nodes = [
            TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)", TextType.NORMAL),
            TextNode("This is text with ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.NORMAL),
        ]
        expected = [
            TextNode("This is text with a ", TextType.NORMAL, None),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"), 
            TextNode("This is text with ", TextType.NORMAL, None),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertEqual(split_nodes_image(nodes), expected)

    def test_no_nodes_image(self):
        expected = []
        self.assertEqual(split_nodes_image([]), expected)

    def test_empty_text_image(self):
        node = TextNode("", TextType.NORMAL)
        with self.assertRaises(ValueError) as context:
            split_nodes_image([node])
        self.assertEqual(str(context.exception), "TextNode Text cannot be empty")

    def test_null_text_image(self):
        node = TextNode(None, TextType.NORMAL)
        expected = []
        self.assertEqual(split_nodes_image([node]), expected)

    def test_abnormal_type_image(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)", TextType.IMAGE)
        expected = [TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)", TextType.IMAGE)]
        self.assertEqual(split_nodes_image([node]), expected)

    def test_empty_url_image(self):
        node = TextNode("This is text with a ![rick roll]", TextType.NORMAL)
        expected = [TextNode("This is text with a ![rick roll]", TextType.NORMAL)]
        self.assertEqual(split_nodes_image([node]), expected)

#

    def test_split_node_link(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL)
        expected = [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(split_nodes_link([node]), expected)

    def test_multiple_nodes_link(self):
        nodes = [
            TextNode("This is text with a link [to boot dev](https://www.boot.dev)", TextType.NORMAL),
            TextNode("This is text with a link [to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL),
        ]
        expected = [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(split_nodes_link(nodes), expected)

    def test_no_nodes_link(self):
        expected = []
        self.assertEqual(split_nodes_link([]), expected)

    def test_empty_text_link(self):
        node = TextNode("", TextType.NORMAL)
        with self.assertRaises(ValueError) as context:
            split_nodes_link([node])
        self.assertEqual(str(context.exception), "TextNode Text cannot be empty")

    def test_null_text_link(self):
        node = TextNode(None, TextType.NORMAL)
        expected = []
        self.assertEqual(split_nodes_link([node]), expected)

    def test_abnormal_type_link(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev)", TextType.LINK)
        expected = [TextNode("This is text with a link [to boot dev](https://www.boot.dev)", TextType.LINK)]
        self.assertEqual(split_nodes_link([node]), expected)

    def test_empty_url_link(self):
        node = TextNode("This is text with a ![rick roll]", TextType.NORMAL)
        expected = [TextNode("This is text with a ![rick roll]", TextType.NORMAL)]
        self.assertEqual(split_nodes_link([node]), expected)
        
            

        

if __name__ == "__main__":
    unittest.main()