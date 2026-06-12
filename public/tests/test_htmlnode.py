import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_diff_tag(self):
        node1 = HTMLNode(tag="p", value="Hello")
        node2 = HTMLNode(tag="div", value="Hello")

        self.assertNotEqual(node1, node2)


    def test_diff_child(self):
        node1 = HTMLNode(
            tag="ul",
            children=[
                HTMLNode(tag="li", value="Item 1")
            ]
        )

        node2 = HTMLNode(
            tag="ul",
            children=[
                HTMLNode(tag="li", value="Item 2")
            ]
        )

        self.assertNotEqual(node1, node2)

    def test_props_to_html(self):
        node = HTMLNode(tag="p")

        self.assertEqual(node.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()