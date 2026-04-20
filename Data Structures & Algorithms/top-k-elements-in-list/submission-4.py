class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        new_arr = []

        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)
        
        for n in range(k):
            highestKey = 0
            highestVal = 0
            for key in hashmap:
                if hashmap[key] > highestVal:
                    highestVal = hashmap[key]
                    highestKey = key
            new_arr.append(highestKey)
            del hashmap[highestKey]

        return new_arr