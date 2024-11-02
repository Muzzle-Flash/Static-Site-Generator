from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    def process_text(text):
        #print(f"processing {text} as type {text_type}\n")
        is_valid_delimiter_pair = lambda text, pos, delimiter: not (text[pos:pos + len(delimiter) * 2] == delimiter * 2 or text[max(0, pos - len(delimiter)):pos + len(delimiter)] == delimiter * 2)


        def find_next_valid_delim(start_pos):
            #print(f"Searching from position {start_pos}")
            first_pos = text.find(delimiter, start_pos)
            #print(f"First pos: {first_pos}")
            if first_pos != -1 and not is_valid_delimiter_pair(text, first_pos, delimiter):
                return find_next_valid_delim(first_pos + len(delimiter))
            if first_pos == -1:
                return -1, -1
            second_pos = text.find(delimiter, first_pos+len(delimiter))
            #print(f"Second pos: {second_pos}")
            if second_pos == -1:
                #print(f"Failed to find closing delimiter in: '{text}'\n")
                raise ValueError("Closing delimiter not found")
            content = text[first_pos+len(delimiter):second_pos]
            if content.strip() != '':
                #print(f"found valid delimiter pair {text[first_pos:second_pos+len(delimiter)]} at: {first_pos}:{second_pos}\n")
                return first_pos, second_pos
            if content.strip() == '':
                #print(f"found empty delimiter pair {text[first_pos:second_pos+len(delimiter)]} at: {first_pos}:{second_pos}\n")
                return find_next_valid_delim(second_pos + len(delimiter))
        
        
        first_pos, second_pos = find_next_valid_delim(0)
        if first_pos == -1:
            #print(f"returning node {[TextNode(text, TextType.NORMAL)] if text else []}\n")
            return [TextNode(text, TextType.NORMAL)] if text else []
        
        before = text[:first_pos]
        content = text[first_pos + len(delimiter):second_pos]
        after = text[second_pos + len(delimiter):]

        result = []
        if before:
            result.extend(process_text(before))
        result.append(TextNode(content, text_type))
        if after:
            result.extend(process_text(after))
        #print(f"returning nodes {result}\n")
        return result


    new_nodes = []
    for node in old_nodes:
        if delimiter == '':
            raise ValueError("Delimiter cannot be empty")
        if not delimiter:
            raise ValueError("No Delimiter provided")
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        new_nodes.extend(process_text(node.text))
    #print(f"final nodes: {new_nodes}")
    return new_nodes