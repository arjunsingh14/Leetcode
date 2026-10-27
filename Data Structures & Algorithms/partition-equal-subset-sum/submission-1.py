class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        cache = {}

        def helper(i, currSum):
            if total - currSum == currSum:
                return True
            if i >= n:
                return False
            if (i, currSum) in cache:
                return cache[(i, currSum)]
            
            cache[(i, currSum)] = helper(i + 1, currSum) or helper(i + 1, currSum + nums[i])
            return cache[(i, currSum)]
        return helper(0, 0)
