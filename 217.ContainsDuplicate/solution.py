# Solution with Hashset Space Complexity : O(1) Time Complexity : O(N) 
class Solution:
    def containsDuplicate(self, nums:List[int]) -> bool :
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False