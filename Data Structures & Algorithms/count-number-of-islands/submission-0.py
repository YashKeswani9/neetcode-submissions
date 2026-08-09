class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        ans = 0
        visited = set()

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r,c))
            directions = [[1,0], [0,1], [-1, 0], [0, -1]]

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r in range(rows) and c in range(cols) 
                        and grid[r][c] == "1" and 
                        (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c)) 

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    ans += 1
        
        return ans
