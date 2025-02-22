class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, 1
        area = 0
        while l < n:
            # find left
            while l < n and height[l] == 0:
                l += 1
            # l is now selected

            # find right
            r = l + 1
            while r < n and height[r] < height [l]:
                r += 1
            # r is now selected

            #Calculate Area
            if r < n:
                for i in range(l+1,r):
                    area += min(height[l],height[r]) - height[i]
            
            l = r
        return area