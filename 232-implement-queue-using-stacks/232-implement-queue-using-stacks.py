class MyQueue:

    def __init__(self):
        self.stack = []
        self.revstack = []

    def push(self, x: int) -> None:
        while self.stack:
            self.revstack.append(self.stack.pop())
            
        self.stack.append(x)
        while self.revstack:
            self.stack.append(self.revstack.pop())
        
        
    def pop(self) -> int:
        print(self.stack)
        if self.stack: 
            return self.stack.pop()

    def peek(self) -> int:
        data = self.stack.pop()
        self.stack.append(data)
        print(self.stack)
        return data
    def empty(self) -> bool:
        data = None
        if self.stack : 
            data = self.stack.pop()
        if data : 
            self.stack.append(data) 
            return False
            
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(1)
# obj.push(2)
# obj.push(3)
# obj.push(4)

# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()