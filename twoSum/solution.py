#Brute Force Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(i+1, len(nums)):
            complement: int = target - nums[i]
            if complement in hashmap and hashmap[complement] != i :
                return [i, hashmap[complement]]
        # if a pair is not found return empty array
        return []
    
class Solution2:
    def twoSum(self, nums:List[int], target:int) ->List[int] :
        hashtable = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashtable:
                return [i, hashtable[complement]]
            else:
                hashtable[complement] = i
        return []