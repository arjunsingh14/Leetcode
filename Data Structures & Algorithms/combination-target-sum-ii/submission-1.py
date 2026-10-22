class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def helper(i, currSum, curr):
            nonlocal res
            if currSum == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or currSum > target:
                return
            curr.append(candidates[i])
            helper(i + 1, currSum + candidates[i], curr)
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            curr.pop()
            helper(i + 1, currSum, curr)
        helper(0, 0, [])
        return res
        