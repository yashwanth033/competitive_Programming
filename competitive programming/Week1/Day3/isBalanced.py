def isBalanced(root):
    if root is None: 
        return True  
    
    depths = []
    nodes = []
    nodes.append((root, 0))
    while len(nodes):  
        node, depth = nodes.pop()
        if (not node.left) and (not node.right):  
            if depth not in depths: 
                depths.append(depth) 
            if ((len(depths) > 2) or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1)): 
                return False
        else:
            if node.left:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))
    return True

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

if __name__ == '__main__':
    tree = BinaryTreeNode(50)
    left = tree.insert_left(30)
    right = tree.insert_right(80)
    left.insert_left(20)
    left.insert_right(60)
    right.insert_left(70)
    right.insert_right(90)
    print(isBalanced(tree))