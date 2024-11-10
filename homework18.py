# მოიძიეთ ინფორმაცია ბინარულ ხეზე და დაწერეთ 
# დაბეჭდვის ფუნქციები printLeafNodes და countEdges


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLeafNodes(root):
    if root == None:
        return
    print(root.data, end = ': ')

    if root.left != None:
        print("L", root.left.data, end=' ')

    if root.right != None:
        print("R", root.left.data, end= ' ')

    printLeafNodes(root.left)
    printLeafNodes(root.right)
    

# def countEdges( root: BinaryTreeNode):
#     def pre(node):
#         if not node: return 0
#         return pre(node.left) + pre(node.right)+1
#     return pre(root)

def countEdges(root: BinaryTreeNode):
    if not root: return 0
    def left_height(node):
        if not node: return 0
        return 1 + left_height(node.left)
    
    def right_height(node):
        if not node: return 0
        return 1 + right_height(node.right)
    
    lef, rig = left_height(root), right_height(root)

    if lef > rig:
        return 1 + countEdges(root.left) + countEdges(root.right)
    else:
        return (2** lef) -1
    


bt1 = BinaryTreeNode(1)
bt2 = BinaryTreeNode(2)
bt3 = BinaryTreeNode(3)

bt1.left = bt2
bt1.right = bt3


printLeafNodes(bt1)

print("Count of edges:", countEdges(bt1))

