class Node:
    def __init__(self,prev,next,val):
        self.prev = prev
        self.next = next
        self.val = val

class MyLinkedList:

    def printRec(self, head):
        data = ""
        while (head != None):
            data = data + " " + f"{head.val}"
            head = head.next

        print(data)
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        node = self.head
        itr = 0
        while(node):
            if(itr == index):
                return node.val
            node = node.next
            itr = itr + 1
        return -1

    def addAtHead(self, val: int) -> None:
        if self.head == None:
            self.head = Node(None, None, val)
        else:
            current = Node(None, self.head, val)
            self.head.prev = current
            self.head = current

    def addAtTail(self, val: int) -> None:
        node = self.head
        if not node :
                self.addAtHead(val)
        else:        
            newNode = Node(None,None,val)
            while(node.next):
                node = node.next
            node.next = newNode
            newNode.prev = node
        # node.next =

    def addAtIndex(self, index: int, val: int) -> None:
        node = self.head
        itr = 0
        NewNode = Node(None,None,val)
        prevnode = None
        reachedend = 1
        if(not node and index == 0):
            self.addAtHead(val)
            reachedend = 0
        while(node):
            if(index == 0):
                print("in here")
                self.addAtHead(val)
                reachedend = 0
                break
            if(itr == index):
                # temp = node
                node.prev.next = NewNode
                NewNode.prev = node.prev
                NewNode.next = node
                node.prev = NewNode
                reachedend = 0
                break
            prevnode = node
            node = node.next
            itr = itr+1
        # print(node.val)
        # print(itr,index)
        if (reachedend == 1 and (index-itr == 0)):
         prevnode.next = NewNode
         NewNode.prev = prevnode


    def deleteAtIndex(self, index: int) -> None:
        node = self.head
        itr = 0
        while(node):
            if(itr == index):
                # temp = node

                if(itr == 0 ):
                    if(node.next):
                     node = node.next
                     node.prev = None
                     self.head = node
                    else:
                     self.head = None

                if (node.prev):
                  node.prev.next = node.next
                if(node.next):
                  node.next.prev = node.prev
                break
            node = node.next
            itr = itr+1
