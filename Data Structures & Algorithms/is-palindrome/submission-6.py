class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if not self.isAlNum(s[l]):
                l += 1
                continue
            if not self.isAlNum(s[r]):
                r -= 1
                continue
                
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1

            else:
                return False

        return True

    def isAlNum(self, s):
        return (
            ord('a') <= ord(s) <= ord('z') or
            ord('A') <= ord(s) <= ord('Z') or
            ord('0') <= ord(s) <= ord('9')
        )