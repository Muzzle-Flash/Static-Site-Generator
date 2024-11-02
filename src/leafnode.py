from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, props = None, tag = None):
        super().__init__(tag, value, None, props)
        
    
    def to_html(self):
        if not self.tag:
            return self.value
        if self.value == None:
            raise ValueError("LeafNode must have a Value")
        if self.props:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        return f'<{self.tag}>{self.value}</{self.tag}>'
            
