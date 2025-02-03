class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count_evens = {}
        for num in nums:
            if num % 2 == 0:
                count_evens[num] = 1 + count_evens.get(num, 0)
        
        freq = [[] for i in range(len(nums) + 1)]
        for num, count  in count_evens.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            if len(freq[i]) == 1:
                return freq[i][0]
            elif len(freq[i]) > 1:
                return min(freq[i])
        return -1
            
        
        