from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s2:
            return False
        s1Count = defaultdict(int)
        s2Count = defaultdict(int)
        for c in range(ord("a"), ord("z") + 1):
            s1Count[chr(c)] = 0
            s2Count[chr(c)] = 0
        
        for c in s1:
            s1Count[c] += 1

        l = 0
        n = len(s1)
        print(s1Count)
        for r in range(len(s2)):
            s2Count[s2[r]] += 1
            while r - l + 1 > n:
                s2Count[s2[l]] -= 1
                l += 1
            if s2Count == s1Count:
                return True

        return False


