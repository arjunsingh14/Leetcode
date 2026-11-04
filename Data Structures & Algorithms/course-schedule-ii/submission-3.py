class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        for crs, preq in prerequisites:
            adjList[crs].append(preq)
        
        visit, path = set(), set()
        topSort = []
        def dfs(node):
            if node in path:
                return False
            if node in visit:
                return True
            path.add(node)
            for nei in adjList[node]:
                if not dfs(nei):
                    return False
            path.remove(node)
            visit.add(node)
            topSort.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return topSort