from collections import OrderedDict


class Node :
    def __init__(self,data):
        self.data = data
        self.nodes = []
        self.wordWeight = 0

        
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

        currentnode.wordWeight = currentnode.wordWeight + 1        
    def printtrie(self):
        q = [self.head]
        data = " "
        while q:
             current = q.pop(0)
             data = data + f'{current.data}'
             for node in current.nodes:
                q.append(node)
        print(data) 

    def getWords(self,key):
        pass
        # do dfs to find words

        words = OrderedDict()

        def dfs(key,node):
            stack = [(node,'')]
            idx = 0 
            while(stack):
                (currentnode,rootnodeval) = stack.pop()
                if currentnode.wordWeight > 0 :
                    # words.append(rootnodeval + currentnode.data)
                    words[idx] = key + rootnodeval + currentnode.data
                    idx = idx + 1

                for node in currentnode.nodes:
                    stack.append((node,rootnodeval + currentnode.data))  

            return words          



        current = self.head
        matchedkey = ""

        for char in key:
            matchedkeychar = False             
            for node in current.nodes:
                if node.data == char:
                    matchedkeychar = True
                    current = node
                    break
            if not matchedkeychar : break 
            matchedkey = matchedkey + char

        if matchedkey == key: 
          return  dfs(key[0:-1],current)


        return "no matches found" 



            
trie = Trie()
trie.add("GO")
trie.printtrie()

trie.add("GET")
trie.add("GEETA")
trie.printtrie()

trie.add("CHEAT")
trie.add("CHEATER")
trie.add("CRAZY")
trie.printtrie()

print(trie.head.nodes[1].nodes[0].data)
print(trie.getWords("CH"))
