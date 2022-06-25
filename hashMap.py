class MyHashMap:
    def __init__(self):
        self.data = [None for element in range(10)]

    def hashFunction(self,key):
        return (key % 10)

    def get(self,key):
        getAtIndex = self.hashFunction(key)
        if(self.data[getAtIndex] == None):
            return -1
        else:
            return self.data[getAtIndex][1]
    def put(self,key,value):
        insertAtIndex = self.hashFunction(key)
        self.data[insertAtIndex] = [key,value]

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
    myHashMap = MyHashMap()
    myHashMap.put(1, 1)
    myHashMap.get(1)
    pass