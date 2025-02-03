class Solution:
    def topKFrequent(self, nums: List[int], k:int) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        
        sorted_occurences = []
        for key in hashmap:
            sorted_occurences.append([hashmap[key], key])
        sorted_occurences.sort(reverse=True)

        top_k_frequent = []
        for i in range(0,k):
            top_k_frequent.append(sorted_occurences[i][1])

        return top_k_frequent

class Solution:
    def topKFrequent(self, nums: List[int], k:int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + nums.get(num, 0)
        
        freq = [[] for i in range(len(nums) + 1)]
        for num, count in nums.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return []