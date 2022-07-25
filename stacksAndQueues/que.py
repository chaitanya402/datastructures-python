from Node import  Node

class que:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        if not self.head : return True
        else : return False

    def peek(self):
        if  self.head : return self.head.data


    def add(self,data):
        node = Node(data,None)
        if  self.tail :
            self.tail.next = node
        self.tail = node
        if not self.head :
            self.head = node

    def remove(self):
        if self.head :
            data = self.head.data
            self.head = self.head.next
        if not self.head : self.tail = None
        return data



q = que()
print(q.isEmpty())

q.add(1)
q.add(2)
q.add(3)
print(q.peek()) #peek
print(q.remove())
print(q.remove())
print(q.remove())

