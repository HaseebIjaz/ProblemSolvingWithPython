class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1 ,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            else:
                hashmap[nums[i]] = i
        return []


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        A.sort()

        i, j = 0, len(nums) - 1
        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1], A[j][1]),
                        max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []
    
class Solution:
    def twoSum(self, numbers:List[int], target:int) -> List[int]:
        if numbers[(len(numbers) - 2)] + numbers[len(numbers) - 1] < target: return []
        if numbers[0] + numbers[1] > target: return []
        
        l, r = 0, len(numbers) - 1
        while l < r:
            current_sum = numbers[l] + numbers[r]
            if current_sum == target:
                return [l + 1, r + 1]  # 1-based indices
            elif current_sum > target:
                r -= 1  # Reduce sum by moving right pointer left
            else:
                l += 1  # Increase sum by moving left pointer right
        return []