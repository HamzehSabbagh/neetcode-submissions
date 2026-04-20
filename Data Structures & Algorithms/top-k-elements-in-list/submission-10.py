class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        res = []
        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)
                
        for i in range(k):
            highest_key = 0
            highest_value = 0

            for key in hashmap:
                if hashmap[key] > highest_value:
                    highest_key = key
                    highest_value = hashmap[key]

            res.append(highest_key)
            del hashmap[highest_key]

        return res