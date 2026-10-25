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
            visit.add(node)
            path.add(node)
            for nei in adjList[node]:
                if not dfs(nei):
                    return False
            topSort.append(node)
            path.remove(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return topSort
                

        