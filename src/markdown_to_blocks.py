def markdown_to_blocks(markdown):
    line_list = markdown.split("\n\n")
    result = []
    for block in line_list:
        if block.strip():  # if block isn't empty
            # split block into lines and clean each line
            cleaned_lines = [line.strip() for line in block.split("\n")]
            # join the cleaned lines back together
            cleaned_block = "\n".join(cleaned_lines)
            cleaned_block = cleaned_block.strip()
            result.append(cleaned_block)
    return result