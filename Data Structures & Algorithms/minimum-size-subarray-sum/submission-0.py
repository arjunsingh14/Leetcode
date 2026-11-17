class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = float("inf")
        currTotal = 0
        for r in range(len(nums)):
            currTotal += nums[r]
            while currTotal >= target:
                res = min(res, r - l + 1)
                currTotal -= nums[l]
                l += 1
        return res if res != float("inf") else 0