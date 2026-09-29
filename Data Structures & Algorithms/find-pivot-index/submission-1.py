class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        prefixSum = [0] * (len(nums) + 1)
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            prefixSum[i + 1] = prefix
        
        for i in range(1, len(prefixSum)):
            rightWindow = total - prefixSum[i]
            leftWindow = prefixSum[i - 1]
            if rightWindow == leftWindow:
                return i - 1
        return -1
