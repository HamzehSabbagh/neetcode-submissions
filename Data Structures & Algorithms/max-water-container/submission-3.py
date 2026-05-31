class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        highestNumber = 0

        while l < r:
            highestNumber = max((r - l) * min(heights[l], heights[r]), highestNumber)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return highestNumber