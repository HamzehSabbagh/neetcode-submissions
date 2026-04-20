class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sub = Counter(t)
        string = Counter()
        temp = ''
        res = ''
        l, r = 0, 0

        while r < len(s):
            string[s[r]] += 1
            temp += s[r]
            r += 1
            count = 0
            for c in sub:
                if sub[c] <= string[c]:
                    count += 1
                else:
                    count = 0

            while len(sub) <= count:
                if len(temp) < len(res) or res == '':
                    res = temp
                    
                string[s[l]] -= 1
                temp = temp[1:]
                l += 1
                count = 0
                for c in sub:
                    if sub[c] <= string[c]:
                        count += 1
                    else:
                        count = 0
        return res
            
