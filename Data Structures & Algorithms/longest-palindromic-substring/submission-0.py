class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(l, r):
            substr = ""
            maxLength = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLength:
                    substr = s[l:r+1]
                    maxLength = r - l + 1
                l -= 1
                r += 1
            return (substr, maxLength)
        res = ""
        length = 0
        for i in range(len(s)):
            odd, oddLength = helper(i, i)
            even, evenLength = helper(i, i + 1)
            if oddLength > length:
                length = oddLength
                res = odd
            if evenLength > length:
                length = evenLength
                res = even
        return res