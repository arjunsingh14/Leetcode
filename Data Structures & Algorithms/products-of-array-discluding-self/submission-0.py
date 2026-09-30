class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums))
        
        p = 1
        for i in range(len(nums)):
            prefix[i] = p
            p *= nums[i]
        
        p = 1
        for i in range(len(nums) -1, -1, -1):
            prefix[i] *= p
            p *= nums[i]

        return prefix
        