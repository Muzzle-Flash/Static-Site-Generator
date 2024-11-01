import unittest
from markdown_to_blocks import markdown_to_blocks

class test_markdown_to_blocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item"""
        expected_blocks = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item"""
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_extra_blank_lines(self):
        markdown = """# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        


        * This is the first list item in a list block
        * This is a list item
        * This is another list item"""
        expected_blocks = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item"""
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_single_block(self):
        markdown = """* This is the first list item in a list block
        * This is a list item
        * This is another list item"""
        expected_blocks = [
            """* This is the first list item in a list block
* This is a list item
* This is another list item"""
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_mixed_media(self):
        markdown = """# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev) inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item
        
        1. this is the first item in an ordered list
        2. this is the second item
        3. this is the third item"""
        expected_blocks = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev) inside of it",
            """* This is the first list item in a list block
* This is a list item
* This is another list item""",
            """1. this is the first item in an ordered list
        2. this is the second item
        3. this is the third item"""
        ]




if __name__ == "__main__":
    unittest.main()
