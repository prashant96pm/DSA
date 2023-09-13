'''Remove a node from BST'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_min(node):
    while node.left is not None:
        node = node.left
    return node

def removeNode(root, X):
    if root is None:
        return root

    # If the value to be deleted is smaller than the root's value,
    # then it is in the left subtree.
    if X < root.val:
        root.left = removeNode(root.left, X)

    # If the value to be deleted is greater than the root's value,
    # then it is in the right subtree.
    elif X > root.val:
        root.right = removeNode(root.right, X)

    # If the value to be deleted is the same as the root's value,
    # then this is the node to be deleted.
    else:
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children: Get the inorder successor (smallest
        # in the right subtree)
        temp = find_min(root.right)

        # Copy the inorder successor's content to this node
        root.val = temp.val

        # Delete the inorder successor
        root.right = removeNode(root.right, temp.val)

    return root

def inOrderTraversal(root):
    if root:
        inOrderTraversal(root.left)
        print(root.val, end=' ')
        inOrderTraversal(root.right)

# Sample input and usage
if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(6)
    
    X = 6

    print("Inorder traversal before removal:")
    inOrderTraversal(root)
    print()

    root = removeNode(root, X)

    print("Inorder traversal after removal:")
    inOrderTraversal(root)
