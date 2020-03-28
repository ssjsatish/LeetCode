class Tree:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

def isSameTree(root1, root2):
    if root1 is None and root2 is None:
        return True
    else:
        return (root1.data==root2.data) and isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)
    return False