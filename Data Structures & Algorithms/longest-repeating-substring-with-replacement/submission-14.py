class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        highest = 0

        l ,r, con = 0, 0, 0
        
        while r < len(s):
            val = 0
            hashMap[s[r]] = 1 + hashMap.get(s[r], 0)
            if len(hashMap) > 1:
                for key in hashMap:
                    val = max(val, hashMap[key])
        
                if r - l + 1 - val > k:
                    hashMap[s[l]] -= 1
                    if hashMap[s[l]] <= 0:
                        del hashMap[s[l]]
                    highest = max(highest, con)
                    con -= 1
                    l += 1
                    
                    
            con += 1
            r += 1

        return max(highest, con)
            

                
                