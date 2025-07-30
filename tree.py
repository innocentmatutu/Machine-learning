class tree_node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

#pre_order traversal
def pre_order(node):
    if node is None:
        return
    print(node.data,end=',')
    pre_order(node.left)
    pre_order(node.right)
#in_order traversal
def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.data, end=',')
    in_order(node.right)
#post_order traversal
def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.data, end=',')

root = tree_node('R')
nodeA = tree_node('A')
nodeB = tree_node('B')
nodeC = tree_node('C')
nodeD = tree_node('D')
nodeE = tree_node('E')
nodeF = tree_node('F')
nodeG = tree_node('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

print('root.right.left.data:',root.right.left.data)
print('root.left.right.data:',root.left.right.data)
#post_order(root)
#in_order(root)
pre_order(root)