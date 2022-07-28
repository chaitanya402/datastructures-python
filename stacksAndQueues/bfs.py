grid = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]
def numIslands(grid):
    rows = len(grid)
    columns = len(grid[0])
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

    # for r in range(rows):
    #     for c in range(columns):
    #         if grid[r][c] == "1" and (r,c) not in visited:
    #             bfs(grid)
    #             islands = islands + 1
    # return islands