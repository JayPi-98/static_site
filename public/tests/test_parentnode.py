import unittest

from src.parentnode import ParentNode
from src.leafnode import LeafNode


class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_children_props(self):
        child_node = LeafNode("a", "My Spotify playlist", {"href": "https://open.spotify.com/playlist/51XYStwSepk8VYzkrEWDE6"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(), 
            '<div><a href="https://open.spotify.com/playlist/51XYStwSepk8VYzkrEWDE6">My Spotify playlist</a></div>'
            )

    def test_to_html_with_grandchildren_props(self):
        grandchilde_node = LeafNode("a","Casas Diamante", {"href": "https://casasdiamante.com/"})
        child_node = ParentNode("b", [grandchilde_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), '<div><b><a href="https://casasdiamante.com/">Casas Diamante</a></b></div>')

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )
