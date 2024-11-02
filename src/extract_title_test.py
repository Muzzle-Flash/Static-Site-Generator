import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_basic(self):
        markdown = "#  Header? No! Title!"
        expected = "Header? No! Title!"
        self.assertEqual(extract_title(markdown), expected)

    def test_more_than_one_hashmark(self):
        markdown = "## this isn't a title!"
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "Page must have a title!")

    def test_no_hashmark(self):
        markdown = "!This is not a title!"
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "Page must have a title!")


if __name__ == "__main__":
    unittest.main()
