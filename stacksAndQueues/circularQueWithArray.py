class MyCircularQueue:
    def __init__(self,k):
        self.data = [None] *k
        self.head = -1
        self.tail = -1
        self.size = k


    def enQueue(self,data):
       if self.isFull() : return False
       if self.isEmpty() : self.head = 0
       self.tail = (self.tail + 1) % self.size
       self.data[self.tail] = data
       return True

    def deQueue(self):
        if self.isEmpty() : return False
        if(self.head == self.tail):
            self.head = -1
            self.tail = -1
            return True
        self.head = (self.head + 1) % self.size
        return True

    def Front(self):
        if self.isEmpty(): return -1
        return  self.data[self.head]

    def Rear(self):
        if self.isEmpty(): return -1
        return self.data[self.tail]



    def isFull(self):
        return (self.tail + 1 ) % self.size == self.head


    def isEmpty(self):
        return self.head == -1