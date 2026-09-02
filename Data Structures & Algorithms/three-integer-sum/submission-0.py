class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        [-1, -1, 0, 1]
        """
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and nums[i - 1] == a:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = a + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[l], nums[r], a])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
