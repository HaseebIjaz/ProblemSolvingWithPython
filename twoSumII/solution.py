class Solution:
    def twoSum(self, nums:List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement] + 1, i +1]
            else:
                hashmap[nums[i]] = i
        return []
    