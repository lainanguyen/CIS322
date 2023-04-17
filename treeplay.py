class TreeNode:
    root = TreeNode('a')

    b = TreeNode('b')
    b.add_child(TreeNode('d'))
    root.add_child(b)

    c = TreeNode('c')
    c.add_child(TreeNode('e'))
    c.add_child(TreeNode('f'))
    c.add_child(TreeNode('g'))
    root.add_child(c)

    root.print_tree()

    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def print_tree(self, level=0):
        print('  ' * level + str(self.value))
        for child in self.children:
            child.print_tree(level + 1)