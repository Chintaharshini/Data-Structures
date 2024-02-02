class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

def preOrder(root=None):
    """ROOT, LEFT, RIGHT."""
    if root is None:
        return
    print(root.data, end= " ")
    preOrder(root.left)
    preOrder(root.right)
def inOrder(root=None):
    """LEFT,ROOT,RIGHT."""
    if root is None:
        return
    inOrder(root.left)
    print(root.data, end= " ")   
    inOrder(root.right)
def postOrder(root=None):
    """LEFT, RIGHT,ROOT."""
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data, end= " ")
    
class CompleteTree:
    def __init__(self,head=None):
        self.head = head
    def insert(self,data):
        currentNode = self.head
        if currentNode is None:
            currentNode = Node(data)
            self.head = currentNode
        else:
            while currentNode:
                if currentNode.left is None:
                    currentNode.left = Node(data)
                    return
                elif currentNode.right is None:
                    currentNode.right = Node(data)
                    return
                else:
                     currentNode = currentNode.left

tree1 = CompleteTree()
tree1.insert(2)
tree1.insert(7)
tree1.insert(5)
tree1.insert(1)
tree1.insert(6)
tree1.insert(9)
tree1.insert(8)
tree1.insert(11)
tree1.insert(4)

preOrder(tree1.head)
print()
inOrder(tree1.head)
print()
postOrder(tree1.head)
