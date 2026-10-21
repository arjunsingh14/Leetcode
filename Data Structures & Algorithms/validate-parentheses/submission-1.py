class Solution:
    def isValid(self, s: str) -> bool:
        brack = {")" : "(", "}" : "{", "]" : "["}
        stack = []
        for b in s:
            if stack and b in brack and brack[b] == stack[-1]:
                stack.pop()
            else:
                stack.append(b)
            
        return not stack
            