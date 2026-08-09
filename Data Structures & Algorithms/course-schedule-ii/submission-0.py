class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {c: [] for c in range(numCourses)}
        for c, p in prerequisites:
            preMap[c].append(p)

        cycle, visited = set(), set()
        res = []

        def dfs(c):
            if c in cycle:
                return False
            
            if c in visited:
                return True
            
            cycle.add(c)
            for pre in preMap[c]:
                if not dfs(pre):
                    return False
            cycle.remove(c)
            visited.add(c)
            res.append(c)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res