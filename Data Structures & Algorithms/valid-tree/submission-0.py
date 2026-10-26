class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        parents = {}
        rank = {}
        for i in range(n):
            parents[i] = i
            rank[i] = 1

        def find(n):
            if n != parents[n]:
                parents[n] = find(parents[n])
            return parents[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parents[p2] = p1
            elif rank[p2] > rank[p1]:
                parents[p2] = p1
            else:
                parents[p2] = p1
                rank[p1] += 1
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return False
        return True