class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixCount = {0:1}
        prefixSum = 0

        for n in nums:
            prefixSum += n
            needed = prefixSum - k
            res += prefixCount.get(needed, 0)

            prefixCount[prefixSum] = prefixCount.get(prefixSum, 0) + 1
        return res
            
