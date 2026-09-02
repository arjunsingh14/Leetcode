class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Need a map:
        [3, 4, 5, 6]
        {}

        target - 3 = 4
        {3 : 0}

        target - 4 = 3
        {3: 0}

        3 is in map, return current index and index in map
        """

        hashMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[n] = i
        