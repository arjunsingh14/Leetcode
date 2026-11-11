class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3, 4, 5, 6, 7, 0, 1, 2]
        #              l  m      r
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (r + l) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res