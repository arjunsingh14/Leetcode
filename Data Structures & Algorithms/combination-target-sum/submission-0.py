class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def helper(i, currSum):
            nonlocal subset
            if currSum == target:
                res.append(subset.copy())
                return
            if i >= len(nums) or currSum > target:
                return

            helper(i + 1, currSum)
            subset.append(nums[i])
            helper(i, currSum + nums[i])
            subset.pop()
        helper(0, 0)
        return res
            


        