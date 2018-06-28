class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def largest(root):
    while root:
        if not root.right:
            return root.value
        root.right

def second_largest(root):
    if (root is None or (root.left and not root.right)):
        raise ValueError("Need atleast two nodes to get second maximum.")
    while root:
        if(root.left and root.right is None):
            return largest(root.left)
        if(root.right and not root.right.left and not root.left.right):
            return root.value
        root = root.right

if __name__ == '__main__':
    tree = BinaryTreeNode(50)
    left = tree.insert_left(30)
    right = tree.insert_right(70)
    left.insert_left(10)
    left.insert_right(40)
    right.insert_left(60)
    right.insert_right(80)
    print(second_largest(tree))