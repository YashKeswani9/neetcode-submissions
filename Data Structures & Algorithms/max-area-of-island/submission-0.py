class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        visited = set()

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            area = 0

            while q:
                r, c = q.popleft()
                area += 1
                for dr, dc in directions:
                    row = dr + r
                    col = dc + c
                    if (row in range(rows) and col in range(cols) 
                    and grid[row][col] == 1 and (row, col) not in visited):
                        visited.add((row,col))
                        q.append((row, col))
            
            return area


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    visited.add((row, col))
                    maxArea = max(maxArea, bfs(row, col))
        
        return maxArea