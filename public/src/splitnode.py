from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    
    if not delimiter:
        raise Exception("Invalid Markdown syntax")

    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        
        parts = node.text.split(delimiter)

        if len(parts) % 2 == 0:
            raise Exception("Invalid Markdown syntax")        

        for i in range(len(parts)):
            if i % 2 == 0:
                new_nodes.append(TextNode(parts[i],TextType.PLAIN_TEXT))
            else: 
                new_nodes.append(TextNode(parts[i], text_type))
    
    
    return new_nodes