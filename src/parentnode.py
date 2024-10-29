from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, children, tag, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Parents must have a Tag")
        if not self.children:
            raise ValueError("Parents must have Children")
        if not self.props:
            result = f'<{self.tag}>'
        else:
            result = f'<{self.tag}{self.props_to_html()}>'
        for child in self.children:
            result += child.to_html()
        result += f'</{self.tag}>'     
        return result