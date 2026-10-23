class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x, y in points:
            distance = math.sqrt(((x - 0) ** 2) + ((y - 0) ** 2))
            distances.append((distance, x, y))
        heapq.heapify(distances)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(distances)
            res.append([x, y])
            k -= 1
        
        return res