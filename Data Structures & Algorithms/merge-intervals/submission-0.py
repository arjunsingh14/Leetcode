class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for i, interval in enumerate(intervals):
            if i == 0:
                res.append(interval)
                continue
            prev = res[-1]
            if interval[0] <= prev[1]:
                prev = [min(interval[0], prev[0]), max(interval[1], prev[1])]
                res[-1] = prev
                continue
            res.append(interval)
        return res
