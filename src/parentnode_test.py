import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_only_child(self):
        child = LeafNode("turn the lights off!", {"href": "https://www.youtube.com/watch?v=dLrdSC9MVb4"}, "a")
        parent = ParentNode([child], "p", None)
        expected_to_html = '<p><a href="https://www.youtube.com/watch?v=dLrdSC9MVb4">turn the lights off!</a></p>'
        self.assertEqual(parent.to_html(), expected_to_html)
        
    def test_many_children(self):
        child1 = LeafNode("turn the lights off!", None, "b")
        child2 = LeafNode("give me a sign!", None, "b")
        child3 = LeafNode("lets make some evil!", None, "b")
        parent = ParentNode([child1, child2, child3], "p", None)
        expected_to_html = '<p><b>turn the lights off!</b><b>give me a sign!</b><b>lets make some evil!</b></p>'
        self.assertEqual(parent.to_html(), expected_to_html)

    def test_grandparent(self):
        grandchild = LeafNode("turn the lights off!", None, "i")
        child = ParentNode([grandchild], "b", None)
        parent = ParentNode([child], "p", None)
        expected_to_html = '<p><b><i>turn the lights off!</i></b></p>'
        self.assertEqual(parent.to_html(), expected_to_html)
    
    def test_no_children(self):
        parent = ParentNode([], "p", None)
        with self.assertRaises(ValueError) as context:
            parent.to_html()
        self.assertEqual(str(context.exception), "Parents must have Children")

    def test_no_tag(self):
        child = LeafNode("I wanna be in the cavalry!", {"href": "https://www.youtube.com/watch?v=gh2g57CzF7w"}, "a")
        parent = ParentNode([child], None, None)
        with self.assertRaises(ValueError) as context:
            parent.to_html()
        self.assertEqual(str(context.exception), "Parents must have a Tag")
        
    def test_props(self):
        child = LeafNode("turn the lights off!", None, "b")
        parent = ParentNode([child], "a", {"href": "https://www.youtube.com/watch?v=dLrdSC9MVb4"})
        expected_to_html = '<a href="https://www.youtube.com/watch?v=dLrdSC9MVb4"><b>turn the lights off!</b></a>'
        self.assertEqual(parent.to_html(), expected_to_html)

    def test_mixed_children(self):
        child1 = LeafNode("turn the lights off!", None, "b")
        child2 = LeafNode("give me a sign!", None, "i")
        child3 = LeafNode("lets make some evil!", {"href": "https://www.youtube.com/watch?v=0RVeo79yfw0"}, "a")
        parent = ParentNode([child1, child2, child3], "p", None)
        expected_to_html = '<p><b>turn the lights off!</b><i>give me a sign!</i><a href="https://www.youtube.com/watch?v=0RVeo79yfw0">lets make some evil!</a></p>'
        self.assertEqual(parent.to_html(), expected_to_html)

    def test_mixed_children2(self):
        child1 = LeafNode("Hello", None, None)  # Just plain text
        child2 = LeafNode("World", None, "b")   # Bold text
        parent = ParentNode([child1, child2], "p", None)
        expected_to_html = '<p>Hello<b>World</b></p>'
        self.assertEqual(parent.to_html(), expected_to_html)

    def test_grandparents(self):
        grandchild1 = LeafNode("Jeff", None, "i")
        grandchild2 = LeafNode("Max", None, "i")
        child1 = ParentNode([grandchild1, grandchild2], "b", None)
        child2 = LeafNode("Matthew", None, "b")
        parent = ParentNode([child1, child2], "p", None)
        expected_to_html = '<p><b><i>Jeff</i><i>Max</i></b><b>Matthew</b></p>'
        self.assertEqual(parent.to_html(), expected_to_html)

if __name__ == "__main__":
    unittest.main()