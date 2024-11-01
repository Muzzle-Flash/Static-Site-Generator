import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_props(self):
        node = LeafNode("Click me baby one more time!", {"href": "https://www.youtube.com/watch?v=5a9ozuMcMYY"}, "a")
        expected_to_html = '<a href="https://www.youtube.com/watch?v=5a9ozuMcMYY">Click me baby one more time!</a>'
        self.assertEqual(node.to_html(), expected_to_html)

    def test_no_props(self):
        node = LeafNode("turn the lights off!", None, "b")
        expected_to_html = '<b>turn the lights off!</b>'
        self.assertEqual(node.to_html(), expected_to_html)

    def test_no_tag(self):
        node = LeafNode("This is just a raw text dump lol")
        expected_to_html = 'This is just a raw text dump lol'
        self.assertEqual(node.to_html(), expected_to_html)

    def test_no_value(self):
        node = LeafNode(None, {"href": "https://www.youtube.com/watch?v=5a9ozuMcMYY"}, "a")
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "LeafNode must have a Value")
    
    def test_non_string_value(self):
        node = LeafNode(15, {"href": "https://www.youtube.com/watch?v=5a9ozuMcMYY"}, "a")
        expected_to_html = '<a href="https://www.youtube.com/watch?v=5a9ozuMcMYY">15</a>'
        self.assertEqual(node.to_html(), expected_to_html)
if __name__ == "__main__":
    unittest.main()