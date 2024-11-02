def block_to_block_type(block):
    result_debug_msg = lambda type: f"assigning type {type}\n"
    #print(f"\nchecking block: \n'{block}'")
    if block.startswith('#') and block[6] !='#':
        type = "heading"
        #print(result_debug_msg(type))
        return type
    if block.startswith("```") and block.endswith("```"):
        type = "code"
        #print(result_debug_msg(type))
        return type
    if block.startswith('>'):
        lines = block.split("\n")
        if len(set(line[0] for line in lines)) == 1:
            type = "quote"
            #print(result_debug_msg(type))
            return type
    if block.startswith('* '):
        lines = block.split("\n")
        if len(set(line[0:1] for line in lines)) == 1:
            type = "unordered_list"
            #print(result_debug_msg(type))
            return type
    if block[0:block.find(".")].isdigit() and block.find(".") != -1 and block[block.find(".")+1] == ' ':
        lines = block.split("\n")
        item_indices = []
        for line in lines:
            item_indices.append(int(line[0:line.find(".")]))
        expected_indices = [i+1 for i in range(len(item_indices))]
        if item_indices == expected_indices:
            type = "ordered_list"
            #print(result_debug_msg(type))
            return type
            
    type = "paragraph"
    #print(result_debug_msg(type))
    return type
                

        
    