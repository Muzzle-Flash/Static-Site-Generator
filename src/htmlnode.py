class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def __eq__(self, other):
        return (
            isinstance(other, HTMLNode) and
            self.tag == other.tag and
            self.value == other.value and
            self.props == other.props
        )
    def props_to_html(self):
        if not self.props:
            return ''
        return ''.join(f' {key}="{value}"' for key, value in self.props.items())
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'