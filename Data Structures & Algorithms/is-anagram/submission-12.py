class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}

        if len(t) != len(s):
            return False

        for i in range(len(s)):
            hashMap[s[i]] = 1 + hashMap.get(s[i], 0)

        for i in range(len(t)):
            if t[i] in hashMap:
                hashMap[t[i]] -= 1
                if hashMap[t[i]] == 0:
                    del hashMap[t[i]]
            else:
                return False
            

        return True