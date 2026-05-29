class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        n_set = set(nums)

        for n in nums:
            con = 0
            if n - 1 not in nums:
                while n + con in n_set:
                    con += 1
                    longest = max(longest, con)

        return longest