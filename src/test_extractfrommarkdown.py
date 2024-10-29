import unittest
from extractfrommarkdown import extract_markdown_images, extract_markdown_links

class TestExtractFromMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_no_url_image(self):
        text = "This is text with a ![rick roll] and ![obi wan]"
        expected = []
        self.assertEqual(extract_markdown_images(text), expected)

    def test_no_alt_image(self):
        text = "This is text with a (https://i.imgur.com/aKaOqIh.gif) and (https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = []
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_no_url_link(self):
        text = "This is text with a link [to boot dev] and [to youtube]"
        expected = []
        self.assertEqual(extract_markdown_links(text), expected)
    
    def test_no_anchor_link(self):
        text = "This is text with a link (https://www.boot.dev) and (https://www.youtube.com/@bootdotdev)"
        expected = []
        self.assertEqual(extract_markdown_links(text), expected)


if __name__ == "__main__":
    unittest.main()