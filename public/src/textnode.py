from enum import Enum

from leafnode import LeafNode

class TextType(Enum):
    PLAIN_TEXT = "text",
    BOLD_TEXT = "bold",
    ITALIC_TEXT = "italic",
    CODE_TEXT = "code"
    LINK_TEXT = "link"
    IMAGE_TEXT = "image"


class TextNode:
    def __init__(self, text: str, text_type, url= None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other) -> bool:
        return (
            self.text == other.text 
            and self.text_type == other.text_type 
            and self.url == other.url
        )
        

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node: TextNode) -> LeafNode:

        if text_node.text_type not in TextType:
            raise Exception("Not a Text type")
        
        if text_node.text_type == TextType.PLAIN_TEXT:
            return LeafNode(None,text_node.text)
        
        if text_node.text_type == TextType.BOLD_TEXT:
            return LeafNode("b",text_node.text)
        
        if text_node.text_type == TextType.ITALIC_TEXT:
            return LeafNode("i", text_node.text)
        
        if text_node.text_type == TextType.CODE_TEXT:
            return LeafNode("code", text_node.text)
        
        if text_node == TextType.LINK_TEXT:
            return LeafNode("a", text_node, {"href": text_node.url})
        
        if text_node == TextType.IMAGE_TEXT:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        
        return LeafNode(None,text_node.text)