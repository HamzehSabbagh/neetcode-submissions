class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')': '(', ']':'[', '}': '{'}

        for c in s:
            if stack and c in hashmap:
                if stack[-1] == hashmap[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)

        return True if not stack else False
