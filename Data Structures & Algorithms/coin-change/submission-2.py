class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def helper(i, currSum):
            if currSum == 0:
                return 0

            if i >= len(coins) or currSum < 0:
                return float("inf")
            
            if (i, currSum) in cache:
                return cache[(i, currSum)]

            cache[(i, currSum)] = min(helper(i + 1, currSum), 1 + helper(i, currSum - coins[i]))

            return cache[(i, currSum)]


        res = helper(0, amount)
        return res if res != float("inf") else -1