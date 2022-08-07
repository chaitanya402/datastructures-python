"""
stack : DFS
Q : BFS
"""
from typing import List
class Node :
    def __init__(self,val,next,min):
        self.val = val
        self.next = next
        self.min = min

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        rows = len(grid)
        columns = len(grid[0])
        islands = 0
        visited = set()

        def bfs(r, c):
            q = []
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            q.append((r, c))
            visited.add((r, c))

            while q:
                node = q.pop(0)

                for x, y in directions:
                    dx = x + node[0]
                    dy = y + node[1]
                    if (dx in range(rows) and
                            dy in range(columns) and
                            (dx, dy) not in visited and
                            grid[dx][dy] == "1"
                    ):
                        q.append((dx, dy))
                        visited.add((dx, dy))

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands = islands + 1
        return islands

    def openLock(self, deadends: List[str], target: str) -> int:
        # target = '0009'
        direction = [1, -1]
        q = [['0000', 0]]
        visited = set(deadends)
        if '0000' in visited: return -1

        visited.add('0000')


        while q:
            cur, turns = q.pop(0)
            if cur == target:
                return turns
            for idx, i in enumerate(cur):

                for step in direction:
                    switch = (int(i) + step) % 10
                    node = cur[:idx] + f'{switch}' + cur[idx + 1:]
                    if (node not in visited):
                        q.append([node, turns + 1])
                        visited.add(node)
        return -1

    def isValid(self, s: str) -> bool:
        closures = {')': '(',
                    '}': '{',
                    ']': '['
                    }
        stack = []

        for i in s:
            if not stack or i not in closures:
                stack.append(i)
                continue
            temp = stack.pop()
            if (closures[i] != temp or i not in closures):
                stack.append(temp)
                stack.append(i)

        if (not stack): return True

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
           stack = []
           sol = [0 for i in range(len(temperatures))]
           for idx,i in enumerate(temperatures):
               if not stack :
                    stack.append([i,idx])
                    continue
               temp,index = stack.pop()
               stack.append([temp,index])
               while(temp < i and stack):
                    sol[index] = idx - index
                    temp,index = stack.pop()
               stack.append([temp,index])
               stack.append([i,idx])
           return sol

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            result = None
            if i == '+':
                result = int(stack.pop()) + int(stack.pop())
                stack.append(result)
                continue
            elif i == '-':
                result = -1 * (int(stack.pop()) - int(stack.pop()))
                stack.append(result)
                continue
            elif i == '/':
                temp = stack.pop()
                result = int(stack.pop()) / int(temp)

                stack.append(result)
                continue
            elif i == '*':
                result = int(stack.pop()) * int(stack.pop())
                stack.append(result)
                continue
            else:
                stack.append(i)
        return (int(stack.pop()))
        
        
        
        class Solution:
            
            
    ####dfs using stack        
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
           stack = [(-1,0)]
           directions = ['+','-']
           sum_of_route  = 0 
           size =  len(nums) 
           while(stack):
               index,sum = stack.pop()
                
               index = index + 1               

               if index == size  and sum == target:
                   sum_of_route = sum_of_route + 1
               else:
                  if index < size:
                   stack.append((index,sum + nums[index]))
                   stack.append((index,sum - nums[index])) 

                
                
                
           return   sum_of_route   
        
