from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        visit = set()
        for src, dest, weight in times:
            adjList[src].append([dest, weight])

        minHeap = [[0, k]]
        time = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            time = w1
            for n2, w2 in adjList[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, [w1 + w2, n2])
        return time if len(visit) == n else -1


            

        