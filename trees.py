# binary search tree implementation 
class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,value):
            if(value < self.data):
                if(self.left != None):
                    self.left.insert(value)
                else:
                    self.left = Node(value)
            else:
                if(self.right != None):
                    self.right.insert(value)
                else:
                    self.right = Node(value)

    def traverseTree(self):
         if(self.left != None):
             self.left.traverseTree()
         print(self.data)
         if(self.right != None):
             self.right.traverseTree()


if __name__ == "__main__":

    node = Node(10)

    node.insert(5)
    node.insert(15)
    node.insert(8)

    node.traverseTree()


    print(node.right.data)