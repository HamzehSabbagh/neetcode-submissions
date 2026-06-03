class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}

        highest = 0

        l, r = 0, 0

        con = 0
        while r < len(s):
            if s[r] not in hashMap:
                con += 1
                hashMap[s[r]] = 1 + hashMap.get(s[r], 0)
                r += 1
            else:
                con += 1
                hashMap[s[r]] = 1 + hashMap.get(s[r], 0)
                while hashMap[s[r]] > 1:
                    con -= 1
                    hashMap[s[l]] -= 1
                    if hashMap[s[l]] == 0:
                        del hashMap[s[l]]
                    l += 1
                r += 1
            highest = max(highest, con)
            
        return max(highest, con)
