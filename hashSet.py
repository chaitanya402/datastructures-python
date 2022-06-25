class MyHashSet:
    def __init__(self):
        self.data = [None for element in range(10)]

    def hashFunction(self,key):
        return (key % 10)

    def add(self,key):
        insertAtIndex = self.hashFunction(key)
        self.data[insertAtIndex] = key

    def remove(self,key):
        removeAtIndex = self.hashFunction(key)
        self.data[removeAtIndex] = None


    def contains(self,key):
         containsAtIndex = self.hashFunction(key)
         if(self.data[containsAtIndex] == None ):
              return False
         else:
              return True

if __name__ == "__main__":
    myHashSet = MyHashSet()
    myHashSet.add(1)
    print(myHashSet.data)
    print(myHashSet.contains(1))
    print(myHashSet.contains(2))
    pass