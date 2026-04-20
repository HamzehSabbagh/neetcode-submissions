class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}

        if len(s) != len(t):
            return False

        for c in s:
            hash1[c] = 1 + hash1.get(c, 0)
        for c in t:
            hash2[c] = 1 + hash2.get(c, 0)

        for c in hash1:
            if hash1[c] != hash2.get(c, 0):
                return False
        return True