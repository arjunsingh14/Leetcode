class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0] 
        cache = {}
        def helper(i, flag):
            if i >= n or (flag and i == n - 1):
                return 0
            if (i, flag) in cache:
                return cache[(i, flag)]
            cache[(i, flag)] = max(helper(i + 1, flag), nums[i] + helper(i + 2, flag))
            return cache[(i, flag)]

        return max(helper(0, True), helper(1, False))