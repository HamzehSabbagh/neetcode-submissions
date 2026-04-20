class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_set = set(nums)
        longest = 0
        for n in (nums):
            con = 0
            if n - 1 not in n_set:
                while n + con in n_set:
                    con += 1
                if con > longest:
                    longest = con
        return longest