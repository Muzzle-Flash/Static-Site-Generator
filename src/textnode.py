from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        if not self.text:
            raise ValueError("TextNode must have Text")
        self.text_type = text_type
        if not self.text_type:
            raise ValueError("TextNode must have a TextType")
        self.url = url
    def __eq__(self, other):
        return (
            isinstance(other, TextNode) and
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )
    def __repr__(self):
        if self.url is None:
            return f'TextNode({self.text}, {self.text_type})'
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
    