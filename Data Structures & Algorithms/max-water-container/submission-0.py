class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0 , len(heights)  - 1
        maximum = 0
        largest = 0
        while l < r:
            if heights[l] < heights[r]:
                maximum = heights[l] * (r-l)
                if maximum > largest:
                    largest = maximum
                l += 1
            elif heights[r] < heights[l]:
                maximum = heights[r] * (r-l)
                if maximum > largest:
                    largest = maximum
                r -= 1
            else:
                maximum = heights[r] * (r-l)
                if maximum > largest:
                    largest = maximum
                r -= 1
        return largest