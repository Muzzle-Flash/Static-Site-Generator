import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter


class TestParentNode(unittest.TestCase):
    def test_no_terminal_del_in_node(self):
        node = TextNode("**the game plays us for fools", TextType.NORMAL)
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter([node], '**', TextType.BOLD)
        self.assertEqual(str(context.exception), "Closing delimiter not found")

    def test_empty_delimiter_in_node(self):
        node = TextNode("**test", TextType.NORMAL)
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter([node], '', TextType.BOLD)
        self.assertEqual(str(context.exception), "Delimiter cannot be empty")

    def test_empty_text_in_node(self):
        node = TextNode('', TextType.NORMAL)
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter([node], '*', TextType.ITALIC)
        self.assertEqual(str(context.exception), "TextNode Text cannot be empty")

    def test_empty_list(self):
        expected_node = []
        self.assertEqual(split_nodes_delimiter([], '*', TextType.ITALIC), expected_node)
    
    def test_no_list(self):
        with self.assertRaises(TypeError):
            split_nodes_delimiter('**', TextType.BOLD)
    
    def test_multiple_delimited_sections(self):
        node = TextNode("This has `code here` and `more code` in it", TextType.NORMAL)
        expected = [TextNode("This has ", TextType.NORMAL), TextNode("code here", TextType.CODE), TextNode(" and ", TextType.NORMAL), TextNode("more code", TextType.CODE), TextNode(" in it", TextType.NORMAL)]
        self.assertEqual(split_nodes_delimiter([node], '`', TextType.CODE), expected)
    
    def test_extreme_delimiters(self):
        node = TextNode("**THE QUESTLORDS OF INVERNESS RIDE!**", TextType.NORMAL)
        expected = [TextNode("THE QUESTLORDS OF INVERNESS RIDE!", TextType.BOLD)]
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), expected)
    
    def test_whitespace(self):
        node = TextNode("Text ** bold with spaces ** end", TextType.NORMAL)
        expected = [TextNode("Text ", TextType.NORMAL), TextNode(" bold with spaces ", TextType.BOLD), TextNode(" end", TextType.NORMAL)]
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), expected)
    
    def test_consecutive_delimiters(self):
        node = TextNode("Text **bold text** **more bold text**", TextType.NORMAL)
        expected = [TextNode("Text ", TextType.NORMAL), TextNode("bold text", TextType.BOLD), TextNode(" ", TextType.NORMAL), TextNode("more bold text", TextType.BOLD)]
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), expected)
    
    def test_odd_delimiters(self):
        node = TextNode("This is `some text with a |` character` more text", TextType.NORMAL)
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter([node], '`', TextType.CODE)
        self.assertEqual(str(context.exception), "Closing delimiter not found")
    
    def test_mismatched_delimiter(self):
        node = TextNode("$Undead force of terror!$", TextType.NORMAL)
        expected = [TextNode("Undead force of terror!", TextType.ITALIC)]
        self.assertNotEqual(split_nodes_delimiter([node], "*", TextType.ITALIC), expected)
    
    def test_missing_delimiter(self):
        node = TextNode("*Undead force of terror!*", TextType.NORMAL)
        with self.assertRaises(TypeError):
            split_nodes_delimiter([node], None, TextType.ITALIC)

    def test_missing_type(self):
        node = TextNode("*Undead force of terror!*", TextType.NORMAL)
        expected = [TextNode("Undead force of terror!", None)]
        self.assertNotEqual(split_nodes_delimiter([node], "*", TextType.ITALIC), expected)
            

        

if __name__ == "__main__":
    unittest.main()