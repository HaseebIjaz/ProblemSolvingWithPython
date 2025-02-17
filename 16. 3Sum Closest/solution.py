class Solution:
    def threeSumClosest(self, nums:List[int], target:int) -> int:
        if len(nums) == 3: return nums[0] + nums[1] + nums[2]
        closest = float('inf')
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and nums[i - 1] == num:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum > target:
                    r -= 1
                elif threeSum < target:
                    l += 1
                else:
                    return target
                if abs(target - threeSum) < abs(target - closest):
                    closest = threeSum
        return closest