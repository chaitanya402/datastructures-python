from Node import Node

class stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def peek(self):
        return self.top.data

    def push(self,data ):
        node = Node(data,None)
        node.next = self.top
        self.top = node

    def pop(self):
        data = None
        if self.top :
            data = self.top.data
            self.top = self.top.next
        return data



stack = stack()
print(stack.isEmpty())
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.pop())
print(stack.pop())