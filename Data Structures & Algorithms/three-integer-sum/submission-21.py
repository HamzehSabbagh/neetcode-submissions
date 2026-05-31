class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums = sorted(nums)

        l = -1

        while l < len(nums):
            l += 1
            r = len(nums) - 1

            while l < len(nums) and l != 0 and nums[l] == nums[l - 1]:
                l += 1

            m = l + 1
            
            while l < len(nums) and m < r:
                if nums[l] + nums[m] + nums[r] == 0:
                    res.append([nums[l], nums[m], nums[r]])
                    m += 1
                    while m < r and nums[m] == nums[m - 1]:
                        m += 1
                elif nums[l] + nums[m] + nums[r] < 0:
                    m += 1
                else:
                    r -= 1
                    

        return res

            




            