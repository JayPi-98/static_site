import unittest
from textnode import TextNode, TextType
from splitnode import split_nodes_delimiter

class TestSplitNode(unittest.TestCase):

    def test_split_bold(self):
        node = TextNode(
            "This is **bold** text",
            TextType.PLAIN_TEXT
        )

        result = split_nodes_delimiter(
            [node],
            "**",
            TextType.BOLD_TEXT
        )

        self.assertEqual(len(result), 3)

        self.assertEqual(
            result[0],
            TextNode("This is ", TextType.PLAIN_TEXT)
        )

        self.assertEqual(
            result[1],
            TextNode("bold", TextType.BOLD_TEXT)
        )

        self.assertEqual(
            result[2],
            TextNode(" text", TextType.PLAIN_TEXT)
    )