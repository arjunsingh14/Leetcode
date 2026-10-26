class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = {}
        rank = {}
        count = n
        for i in range(n):
            parent[i] = i
            rank[i] = 0
        
        def find(n):
            if n != parent[n]:
                parent[n] = find(parent[n])
            return parent[n]
        
        def union(n1, n2):
            nonlocal count
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return
            if rank[p1] > rank[p2]:
                parent[p2] = p1
            elif rank[p2] > rank[p1]:
                parent[p1] = p2
            else:
                parent[p2] = p1
                rank[p1] += 1
            count -= 1
        
        for n1, n2 in edges:
            union(n1, n2)
        return count