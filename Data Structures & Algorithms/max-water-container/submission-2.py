class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        highest_area = 0
        while l < r:
            area = min(heights[l] ,heights[r]) * (r - l)
            if area > highest_area:
                highest_area = area
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return highest_area