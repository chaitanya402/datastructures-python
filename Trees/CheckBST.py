import sys
INT_MIN = -1 * (sys.maxsize - 1)
INT_MAX = (sys.maxsize )
class Node:
     
     def __init__(self,data):
         self.data = data
         self.left = None
         self.right = None
         
def checkBst(node,min,max):
    if not node:
        return True
    print(node.data,min,max)
    if node.data < min or node.data > max: 
        print(0,node.data,min,max)
        return False
    return checkBst(node.left,min,node.data - 1) and checkBst(node.right,node.data + 1,max)


def isBst(node):
    return checkBst(root,INT_MIN,INT_MAX)
    
    
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)    
print(isBst(root))
