import unittest

from src.leafnode import LeafNode


class TestLeadNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h(self):
        node = LeafNode("h1", "This is my static page")
        self.assertEqual(node.to_html(), "<h1>This is my static page</h1>")

    def test_leaf_to_html_props(self):
        node = LeafNode("a", "Link to my Youtube", {"href": "https://www.youtube.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.youtube.com">Link to my Youtube</a>')
    
