class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_dict = {}

        for i in range(len(nums)):
            if nums[i] in nums_dict:
                if abs(i-nums_dict[nums[i]]) <= k :
                    return True
            nums_dict[nums[i]] = i
        return False
    

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int ) -> bool:
        nums_dict = {}

        for i, num in enumerate(nums):
            if num in nums_dict and  abs(i - nums_dict[num]) <= k:
                return True
            nums_dict[num] = i
        return False