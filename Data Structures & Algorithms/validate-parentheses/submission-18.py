class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        for c in s:
            if c in hashMap:
                if stack and hashMap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        
        if stack:
            return False
        else:
            return True
                

        