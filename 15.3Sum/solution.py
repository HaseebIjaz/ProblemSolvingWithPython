class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        twoSums = {}
        indexMap = {}
        res = []
        for i in range(len(nums)):
            indexMap[nums[i]] = i  
            for j in range(i+1,len(nums)):
                twoSum = nums[i] + nums[j] 
                twoSums[twoSum] = twoSums.get(twoSum, [])
                twoSums[twoSum].append([nums[i], nums[j]])
        
        return res