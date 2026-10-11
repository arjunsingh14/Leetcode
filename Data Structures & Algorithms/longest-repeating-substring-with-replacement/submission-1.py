from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        charCount = defaultdict(int)
        maxF = 0
        res = 0
        for r in range(len(s)):
            charCount[s[r]] += 1
            maxF = max(charCount[s[r]], maxF)
            while (r - l + 1) - maxF > k:
                charCount[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
            
            
