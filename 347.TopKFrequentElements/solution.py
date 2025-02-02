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