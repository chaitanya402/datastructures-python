class Node :
    def __init__(self,data):
        self.data = data
        self.nodes = []
        self.word = False
        
class Trie:
                        
    def __init__(self):
        self.head = Node(0)
    def add(self,input):
        currentnode = self.head
        
        for char in input:
            newnode = Node(char)
            found = False
            for node in currentnode.nodes:
                if node.data == char:
                    print("same child node found")
                    found = True
                    currentnode = node
                    break
            if not found:
                print("no child nodes so appending")
                currentnode.nodes.append(newnode)
                currentnode = newnode
    def printtrie(self):
        q = [self.head]
        data = " "
        while q:
             current = q.pop(0)
             data = data + f'{current.data}'
             for node in current.nodes:
                q.append(node)
        print(data) 
trie = Trie()
trie.add("GO")
trie.printtrie()

trie.add("GET")
trie.printtrie()

trie.add("CHEAT")
trie.printtrie()

print(trie.head.nodes[1].nodes[0].data)
