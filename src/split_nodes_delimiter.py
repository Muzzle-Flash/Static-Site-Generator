from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    def process_text(text):
        first_pos = text.find(delimiter)
        if first_pos == -1:
            return [TextNode(text, TextType.NORMAL)] if text else []
        second_pos = text.find(delimiter, first_pos+1)
        if second_pos == -1:
            raise ValueError("Closing delimiter not found")
        
        result = []
        if first_pos > 0:
            result.append(TextNode(text[:first_pos], TextType.NORMAL))
        result.append(TextNode(text[first_pos + len(delimiter):second_pos], text_type))
        remaining_text = text[second_pos + len(delimiter):]
        result.extend(process_text(remaining_text))
        return result
    
    new_nodes = []
    for node in old_nodes:
        if node.text == '':
            raise ValueError("TextNode Text cannot be empty")
        if delimiter == '':
            raise ValueError("Delimiter cannot be empty")
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        new_nodes.extend(process_text(node.text))
    
    return new_nodes