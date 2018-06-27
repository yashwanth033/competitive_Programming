class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def isValidBST(root):
    return solution(root,-float('inf'),float('inf'))

def solution(node,min_value,max_value):
    if not node:return True
    if node.value <= min_value or node.value >=max_value:return False
    return solution(node.left,min_value,node.value) and solution(node.right,node.value,max_value)

if __name__ == '__main__':
    tree = BinaryTreeNode(50)
    left = tree.insert_left(30)
    right = tree.insert_right(80)
    left.insert_left(20)
    left.insert_right(60)
    right.insert_left(70)
    right.insert_right(90)
    result = isValidBST(tree)
    print(result)