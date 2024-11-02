

def extract_title(markdown):
    if (markdown[0] == '#' and markdown[1] == '#') or markdown[0] != '#':
        raise Exception("Page must have a title!")
    lines = markdown.split("\n")
    for line in lines:
        if line[0] == '#' and line[0:] != '#':
            line = line.strip("#")
            line = line.strip()
            return line
