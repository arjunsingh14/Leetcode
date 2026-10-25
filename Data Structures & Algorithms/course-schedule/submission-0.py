
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for preq, crs in prerequisites:
            adjList[preq].append(crs)
        
        visit = set()
        def dfs(node):
            if not adjList[node]:
                return True
            if node in visit:
                return False
            visit.add(node)
            for nei in adjList[node]:
                if not dfs(nei):
                    return False
            adjList[node] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

            