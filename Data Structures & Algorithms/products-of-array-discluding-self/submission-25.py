class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, i = [], 0
        prod = 1
        zeroes = 0

        while i < len(nums):
            if nums[i] == 0:
                zeroes += 1
            else:
                prod *= nums[i]
            i += 1

        if zeroes > 1:
            return [0] * len(nums)

        elif zeroes == 1:
            for x in range(len(nums)):
                if nums[x] == 0:
                    res.append(prod)
                else:
                    res.append(0)
        
        else:
            for x in range(len(nums)):
                res.append(prod // nums[x])

        return res




            