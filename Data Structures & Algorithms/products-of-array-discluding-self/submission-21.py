class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1] * len(nums)
        prod = 1
        zero = 0
        thereIsAZero = False
        for i in range(len(nums)):
            if nums[i] != 0:
                prod *= nums[i]
            elif nums[i] == 0:
               thereIsAZero = True 
        
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            if zero > 1:
                return [0] * len(nums)
            if zero == 1:
                if nums[i] == 0:
                    arr[i] = prod
                else:
                    arr[i] = 0
            else:
                if thereIsAZero:
                    arr[i] = 0
                else:
                    arr[i] = prod // nums[i]
                
        return arr