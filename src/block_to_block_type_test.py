import unittest
from block_to_block_type import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph_block(self):
        block = """this is a normal paragraph block 
with normal text."""
        expected_type = "paragraph"
        self.assertEqual(block_to_block_type(block), expected_type)

    def test_heading_block(self):
        block = """######this is a heading
it is the head of a page"""
        expected_type = "heading"
        self.assertEqual(block_to_block_type(block), expected_type)

    def test_excessive_hashmarks(self):
        block = """#######this is a heading block
with excessive hashmarks."""
        expected_type = "paragraph"
        self.assertEqual(block_to_block_type(block), expected_type)

    def test_missing_hashmarks(self):
        block = """this is a heading block
with missing hashmarks. oops."""
        expected_type = "paragraph"
        self.assertEqual(block_to_block_type(block), expected_type)

    def test_code_block(self):
        block = """```this is a code block,
it contains mighty code```"""
        expected_type = "code"
        self.assertEqual(block_to_block_type(block), expected_type)

    def test_code_block_without_terminal_delim(self):
        block = """```this is a code block
without a terminal delimiter"""
        expected_type = "paragraph"
        self.assertEqual(block_to_block_type(block), expected_type)

    def test_code_block_without_initial_delim(self):
        block = """this is a code block
without an initial delimiter```"""
        expected_type = "paragraph"
        self.assertEqual(block_to_block_type(block), expected_type)

    def test_code_block_without_delims(self):
        block = """this is a code block
without delimiters. oops."""
        expected_type = "paragraph"
        self.assertEqual(block_to_block_type(block), expected_type)

    def test_code_block_with_insufficient_initial_delim(self):
        block = """``this is a code block
with insufficient initial delimiters```"""
        expected_type = "paragraph"
        self.assertEqual(block_to_block_type(block), expected_type)

    def test_code_block_with_insufficient_terminal_delim(self):
        block = """```this is a code block
with insufficient terminal delimiters``"""
        expected_type = "paragraph"
        self.assertEqual(block_to_block_type(block), expected_type)

    def test_quote_block(self):
        block = """>This is the first line in a quote block
>This is a line in a quote
>This is another line in a quote"""
        expected_type = "quote"
        self.assertEqual(block_to_block_type(block), expected_type)

    def test_inconsistent_quote_block(self):
        block = """>This is the first line in a quote block
This is a line in a quote that's inconsistent
>This is another line in a quote"""
        expected_type = "paragraph"
        self.assertEqual(block_to_block_type(block), expected_type)

    def test_unordered_list_block(self):
        block = """* This is the first list item in a list block
* This is a list item
* This is another list item"""
        expected_type = "unordered_list"
        self.assertEqual(block_to_block_type(block), expected_type)
        
    def test_no_space_unordered_list_block(self):
        block = """*This is the first list item in a list block without spaces after asterisks
*This is a list item
*This is another list item"""
        expected_type = "paragraph"
        self.assertEqual(block_to_block_type(block), expected_type)

    def test_inconsistent_unordered_list_block(self):
        block = """* This is the first list item in a list block
This is a list item that's inconsistent
* This is another list item"""
        expected_type = "paragraph"
        self.assertEqual(block_to_block_type(block), expected_type)

    def test_ordered_list_block(self):
        block = """1. This is the first list item in a list block
2. This is the second list item
3. This is the third list item
4. This is the fourth list item"""
        expected_type = "ordered_list"
        self.assertEqual(block_to_block_type(block), expected_type)

    def test_disorganized_ordered_list_block(self):
        block = """1. This is the first list item in a list block
4. This is the fourth list item? That's not right
3. This is the third list item
2. This is the second list item? What's going on?!"""
        expected_type = "paragraph"
        self.assertEqual(block_to_block_type(block), expected_type)

    def test_skipping_ordered_list_block(self):
        block = """1. This is the first list item in a list block
2. This is the second list item
4. This is the third list item
5. This is the fourth list item"""
        expected_type = "paragraph"
        self.assertEqual(block_to_block_type(block), expected_type)


if __name__ == "__main__":
    unittest.main()
