class UnionFind:
    def __init__(self, n):
        self.parents = {}
        self.rank = {}
        for i in range(1, n + 1):
            self.parents[i] = i
            self.rank[i] = 0
    def find(self, n):
        if n != self.parents[n]:
            self.parents[n] = self.find(self.parents[n])
        return self.parents[n]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parents[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.parents[p1] = p2
        else:
            self.parents[p2] = p1
            self.rank[p1] += 1
        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union = UnionFind(len(edges))
        for n1, n2 in edges:
            if not union.union(n1, n2):
                return [n1, n2]
        