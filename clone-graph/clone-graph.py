"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
            
            if node is None :  return None
            if node.neighbors is None : return Node(node.val)
            
            newNodeVals = {}
            stack = [node]
            while stack :
                current = stack.pop()
                newNode = Node(current.val)
                if current.val not in newNodeVals:
                    newNodeVals[current.val] = newNode
                    # stack.append(current)     

                    
                for i in current.neighbors:
                        if i.val not in newNodeVals:
                            stack.append(i) 
                            newNodeVals[i.val] = Node(i.val)
                        newNodeVals[current.val].neighbors.append(newNodeVals[i.val])  

            return(newNodeVals[node.val])
            

                
                
        
        