class Node:
    def __init__(self,data,next):
        self.value = data
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.node = Node(None,None)



    def add(self,data):
        node = self.node
        while(1):
            if(self.head == None):
                self.head = data
                self.node = Node(data,None)
                break
            else:
                if(node.next != None):
                    node = node.next
                else:
                    node.next = Node(data,None)
                    break



    def printLinked(self):
        node = self.node
        value = ""
        while(1):
            if(self.head == None):
                print("empty array")
                break
            else:
                value = f"{value} {node.value} "
                if(node.next != None):
                    node = node.next
                else:
                    break
        print(value)
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if(self.head != None):
            search = 0
            node = self.node
            while(1):
                if (index == search ):
                     print(node.value)
                     break
                else:
                    if(node.next == None):
                        print("reached end")
                        break
                    else:
                        node = node.next
                        search += 1
        else:
            print("empty list")


    def addAtHead(self, val):
        """
        :type index: int
        :rtype: int
        """
        if(self.head != None):
            self.head = val
            self.node.value = val

        else:
            self.head = val
            self.node = Node(val,None)

    def addAtIndex(self, val ,index):
        """
        :type index: int
        :rtype: int
        """
        if(self.head != None):
            search = 0
            node = self.node
            prevNode = Node(None,None)
            newNode = Node(val,None)
            while(1):
                if(index == 0 ):
                   self.addAtHead(val)
                   break
                elif(search  == index):
                   newNode.next = node.next
                   prevNode.next = newNode
                   break
                else:
                    if(node.next == None):
                        print("reached the end")
                        break
                    else:
                        print(node.value)
                        prevNode = node
                        node = node.next
                        search += 1

        else:
            if(index > 0 ):
                print("cannot insert at this level as there are no elements")
            else :
                self.head = val
                self.node = Node(val,None)


    def addAtTail(self, val ):
        """
        :type index: int
        :rtype: int
        """
        if(self.head != None):
            node = self.node
            newNode = Node(val,None)
            while(node.next):
                node = node.next
            node.next = newNode
        else:
                self.head = val
                self.node = Node(val,None)

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: int
        """
        if(self.head != None):
            search = 0
            node = self.node
            prevNode = node
            while(1):
                if(search  == index):
                   # if(index == 0 ):
                   #     node = node.next
                   #
                   # else:
                   prevNode.next = node.next
                   break
                else:
                    if(node.next == None):
                        print("reached the end")
                        break
                    else:
                        prevNode = node
                        node = node.next
                        search += 1

        else:
            print("cannot delete at this level as there are no elements")

if __name__ == "__main__":
    l1 = MyLinkedList()
    l1.add(2)
    l1.add(3)
    l1.add(4)
    l1.add(5)
    l1.printLinked()
    l1.get(2)
    l1.printLinked()
    l1.addAtHead(10)
    l1.printLinked()
    l1.addAtIndex(2,4)
    l1.printLinked()
    l1.addAtTail(999)
    l1.addAtTail(1000)
    l1.printLinked()
    l1.deleteAtIndex(0)
    l1.printLinked()
