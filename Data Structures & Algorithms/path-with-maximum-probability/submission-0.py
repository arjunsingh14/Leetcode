class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjList = defaultdict(list)
        for i in range(len(edges)):
            n1, n2 = edges[i]
            adjList[n1].append([n2, succProb[i]])
            adjList[n2].append([n1, succProb[i]])

        maxHeap = [[1, start_node]]
        heapq.heapify_max(maxHeap)
        visit = set()
        while maxHeap:
            prob, node = heapq.heappop_max(maxHeap)
            if node == end_node:
                return prob
            if node in visit:
                continue
            visit.add(node)
            for nei, prob2 in adjList[node]:
                heapq.heappush_max(maxHeap, [prob * prob2, nei])
        return 0
            
        
        
            
        
        