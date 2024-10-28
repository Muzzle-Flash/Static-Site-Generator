import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_text_type(self):
        node = TextNode("You gotta flip it turnways!", TextType.ITALIC)
        node2 = TextNode("You gotta flip it turnways!", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_text(self):
        node = TextNode("You gotta flip it turnways!", TextType.BOLD)
        node2 = TextNode("IT KEEPS HAPPENNING!", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_url(self):
        node = TextNode("You gotta flip it turnways!", TextType.LINK, "https://www.homestuck.com/story/1349")
        node2 = TextNode("You gotta flip it turnways!", TextType.LINK, "https://www.homestuck.com/sweet-bro-and-hella-jeff/10")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()