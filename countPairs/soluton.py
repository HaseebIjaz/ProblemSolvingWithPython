class Solution:
    def countPairs(self, nums:List[int], target: int) ->int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                count += 1
        return count