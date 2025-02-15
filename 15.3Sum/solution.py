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
        
        for twoSum in twoSums:
            complement = target - twoSum
            if complement in indexMap:
                k = indexMap[complement]
                for ij in twoSums[twoSum]:
                    i,j = ij
                    if i != j and j !=k and i!= k:
                        res.append([i,j,k])
        return res

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
        
        for twoSum in twoSums:
            complement = target - twoSum
            if complement in indexMap:
                k = indexMap[complement]
                for ij in twoSums[twoSum]:
                    i,j = ij
                    if i != j and j !=k and i!= k:
                        res.append([i,j,k])
        return res