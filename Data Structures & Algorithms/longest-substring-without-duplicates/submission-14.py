class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0 , 0
        count = 0
        highest_count = 0
        hashset = {}

        while r != len(s) and len(s) != 0:
            if s[r] not in hashset:
                hashset[s[r]] = set()
                r += 1
                count += 1
            else:
                l += 1
                hashset = {}
                hashset[s[l]] = set()
                r = l + 1
                highest_count = max(highest_count, count)
                count = 1
        return max(highest_count, count)