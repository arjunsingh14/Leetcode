class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def helper(i, currSum, coinCount):
            if currSum == 0:
                return 0

            if i >= len(coins) or currSum < 0:
                return float("inf")
            
            if (i, currSum) in cache:
                return cache[(i, currSum)]

            cache[(i, currSum)] = min(helper(i + 1, currSum, coinCount), 1 + helper(i, currSum - coins[i], coinCount + 1))

            return cache[(i, currSum)]


        res = helper(0, amount, 0)
        return res if res != float("inf") else -1