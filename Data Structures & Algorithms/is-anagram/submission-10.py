class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i], 0)

        for i in range(len(t)):
            if t[i] not in hashS:
                return False
            else:
                if hashS[t[i]] == 0:
                    return False
                else:
                    hashS[t[i]] -= 1


        return True