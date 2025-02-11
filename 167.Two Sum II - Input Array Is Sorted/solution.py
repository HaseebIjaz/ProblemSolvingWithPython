class Solution:
    def twoSum(self, number:List[int], target: int) -> List[int]:
        n = len(numbers)
        if n <= 1: return []

        l, r = 0, n-1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l+1, r+1]
            elif sum < target:
                l += 1
            else:
                r -= 1
        return []