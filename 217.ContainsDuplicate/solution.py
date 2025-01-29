# Solution with Hashset 
# Space Complexity : O(N) Time Complexity : O(N) 
class Solution:
    def containsDuplicate(self, nums:List[int]) -> bool :
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False

# Solution with Hashset Length
# Space Complexity : O(N) Time Complexity : O(N) 

class Solution:
    def containsDuplicate(self, nums:List[int]) -> bool:
        return len(set(nums)) < len(nums) 


## Solution with Sorted Array
## Time Complexity O(NlogN)
## Space Complexity O(1) or O(n) depending on sorting algo
class Solution:
    def containsDuplicate(self, nums:List[int]) -> bool:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
    
## Brute Force
## Space Complexity O(n squared)
## Time Complexity O(1)
class Solution:
    def containsDuplicate(self, nums:List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False