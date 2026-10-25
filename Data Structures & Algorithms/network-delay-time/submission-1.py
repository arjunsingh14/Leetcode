class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for s, d, w in times:
            adjList[s].append([d, w])
        minHeap = [[0, k]]
        heapq.heapify(minHeap)
        visit = set()
        time = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            if len(visit) == n - 1:
                return w1
            visit.add(n1)
            for n2, w2 in adjList[n1]:
                heapq.heappush(minHeap, [w1 + w2, n2])
        return -1

