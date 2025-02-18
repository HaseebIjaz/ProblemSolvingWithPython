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
    
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n == 2: return min(height[0],height[1])
        max_area = 0
        l, r = 0, n-1
        while l< r:
            h = min(height[l],height[r])
            w = r - l
            area = h * w
            max_area = max(area, max_area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_area