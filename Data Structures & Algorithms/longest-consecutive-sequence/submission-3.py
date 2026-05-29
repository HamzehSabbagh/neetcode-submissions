class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestCon = 0
        numsSet = set(nums)
        for i in range(len(nums)):
            con = 0
            if nums[i] - 1 not in numsSet:
                con = 0
                while nums[i] + con in numsSet:
                    con += 1
                    longestCon = max(longestCon, con)

        return longestCon
            
