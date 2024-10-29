#def process_text(text, type):
        result = []
        if type == "img":
             while text:
                images = extract_markdown_images(text)
                if not images:
                    result.append(TextNode(text, TextType.NORMAL))
                    break            
                alt, url = images[0]
                before, markdown, after = text.partition(f"![{alt}]({url})")

                if before:
                    result.append(TextNode(before, TextType.NORMAL))

                result.append(TextNode(alt, TextType.IMAGE, url))
                text = after

        if type == "link":
             while text:
                images = extract_markdown_links(text)
                if not images:
                    result.append(TextNode(text, TextType.NORMAL))
                    break            
                anchor, url = images[0]
                before, markdown, after = text.partition(f"[{anchor}]({url})")

                if before:
                    result.append(TextNode(before, TextType.NORMAL))

                result.append(TextNode(anchor, TextType.IMAGE, url))
                text = after

        return result

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text == '':
            raise ValueError("TextNode Text cannot be empty")
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
        else:
            new_nodes.extend(process_text(node.text, "img"))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text == '':
            raise ValueError("TextNode Text cannot be empty")
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
        else:
            new_nodes.extend(process_text(node.text, "link"))
    return new_nodes