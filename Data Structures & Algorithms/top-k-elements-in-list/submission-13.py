class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        res = []

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
            
        for i in range(k):
            highestVal = 0
            highestKey = 0

            for key in hashmap:
                if hashmap[key] > highestVal:
                    highestVal = hashmap[key]
                    highestKey = key

            del hashmap[highestKey]
            res.append(highestKey)

        return res

                
