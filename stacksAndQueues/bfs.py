grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]


print(grid)

directions = [(0,-1),(0,1),(1 , 0),(-1 , 0)]

print("hello")
    
length = len(grid[0])    
r,c = 0,0
q= []
q.append((r,c))
print(q)
while(q):
    for node in q:
        for x,y in directions:
            
            cdx,cdy= node[0]+x,node[1]+y
            if((cdx >= 0) and (cdy >= 0)):
               print(f"{cdx},{cdy},{x},{y} ,{node[0]},{node[1]}")
               q.append((cdx,cdy))
        print(q)
        q.pop(0)
print(q)
