class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def helper(n):
            if n in cache:
                return cache[n]
            if n <= 3:
                cache[n] = max(n, 0)
            else:
                cache[n] = helper(n - 1) + helper(n - 2)
            return cache[n]
        return helper(n)
            