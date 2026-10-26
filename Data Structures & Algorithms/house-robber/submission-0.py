class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def helper(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            cache[i] = max(helper(i + 1), nums[i] + helper(i + 2))
            return cache[i]
        return helper(0)