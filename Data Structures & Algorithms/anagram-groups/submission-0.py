class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(strs[i])

        return list(hashmap.values())