class Solution:
    def maxArea(self, heights:List[int]) -> int:
        if len(heights) == 2: return min(heights[0],heights[1])
        n = len(heights)
        max_area = 0
        for i in range(n):
            for j in range(i+1, n):
                h = min(heights[i], heights[j])
                w = j - i
                width = h * w
                if area > max_area :
                    max_area = area
        return max_area
