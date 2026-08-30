from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        maxarea = 0

        if not grid:
            return 0

        def bfs(r, c):
            grid[r][c] = 0
            queue.append((r, c))
            area = 1    
            while queue:
                row, col = queue.popleft()
                for dr, dc in neighbors:
                    nr = row + dr
                    nc = col + dc
                    if nr < 0 or nc < 0 or nr >=ROWS or nc>=COLS or grid[nr][nc] == 0:
                        continue
                    queue.append((nr, nc))
                    grid[nr][nc] = 0
                    area = area + 1

            print(area)
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    # bfs(r, c)
                    # print(r, c)
                    maxarea = max(bfs(r, c), maxarea)
        
        return maxarea



