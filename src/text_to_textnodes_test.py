import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToHTML(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.NORMAL),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.NORMAL),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_nested_bold_italic(self):
        text = "This is **bold with *italic* inside** text"
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("bold with *italic* inside", TextType.BOLD),
            TextNode(" text", TextType.NORMAL)
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_malformed_delimiters(self):
        text = "This **bold* text *italic** here"
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This ", TextType.NORMAL),
            TextNode("bold* text *italic", TextType.BOLD),
            TextNode(" here", TextType.NORMAL)
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_empty_delimiters(self):
        text = "This ** ** contains empty bold"
        #print(text_to_textnodes(text))
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This ** ** contains empty bold",TextType.NORMAL)
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_empty_delimiters_only(self):
        text = "****"
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("****",TextType.NORMAL)
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_multiple_empty_delimiter_pairs(self):
        text = "**** ** ****"
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("**** ** ****",TextType.NORMAL)
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_mixed_empty_and_valid_delimiters(self):
        text = "**bold** ** ** **more bold**"
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("bold", TextType.BOLD),
            TextNode(" ** ** ", TextType.NORMAL),
            TextNode("more bold", TextType.BOLD)
        ]
        self.assertEqual(nodes, expected_nodes)

if __name__ == "__main__":
    unittest.main()