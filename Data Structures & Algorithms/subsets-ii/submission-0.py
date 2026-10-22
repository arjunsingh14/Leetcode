class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets, res = [], []

        def helper(i):
            nonlocal res, subsets
            if i >= len(nums):
                res.append(subsets.copy())
                return
            subsets.append(nums[i])
            helper(i + 1)

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            subsets.pop()
            helper(i + 1)
        
        helper(0)
        return res
