class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Hash = {}
        s2Hash = {}
        
        for c in s1:
            s1Hash[c] = 1 + s1Hash.get(c, 0)
    
        l, r = 0, 0

        while r < len(s2):
            while r < len(s1) and r < len(s2):
                s2Hash[s2[r]] = 1 + s2Hash.get(s2[r], 0)
                r += 1

            if s1Hash == s2Hash:
                return True

            if s2Hash[s2[l]] < 2:
                del s2Hash[s2[l]]
            else:
                s2Hash[s2[l]] -= 1
            if r < len(s2):
                s2Hash[s2[r]] = 1 + s2Hash.get(s2[r], 0)
                if s1Hash == s2Hash:
                    return True
                l += 1
                r += 1
        
        return False