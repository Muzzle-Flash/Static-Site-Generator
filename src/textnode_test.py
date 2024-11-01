import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_uneq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is an evil text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    def test_missing_text_type(self):
        with self.assertRaises(ValueError) as context:
            node = TextNode("You gotta flip it turnways!", None)
        self.assertEqual(str(context.exception), "TextNode must have a TextType")
    def test_empty_text(self):
        with self.assertRaises(ValueError) as context:
            node = TextNode("", TextType.BOLD)
        self.assertEqual(str(context.exception), "TextNode must have Text")
    def test_missing_text(self):
        with self.assertRaises(ValueError) as context:
            node = TextNode(None, TextType.BOLD)
        self.assertEqual(str(context.exception), "TextNode must have Text")
    def test_empty_url(self):
        node = TextNode("You gotta flip it turnways!", TextType.LINK, "")
        expected = TextNode("You gotta flip it turnways!", TextType.LINK, "")
        self.assertEqual(node, expected)
    def test_missing_url(self):
        node = TextNode("You gotta flip it turnways!", TextType.LINK, None)
        expected = TextNode("You gotta flip it turnways!", TextType.LINK)
        self.assertEqual(node, expected)
    def test_nonstr_text(self):
        node = TextNode(1650, TextType.ITALIC, None)
        expected_node = TextNode(1650, TextType.ITALIC, None)
        self.assertEqual(node, expected_node)


if __name__ == "__main__":
    unittest.main()