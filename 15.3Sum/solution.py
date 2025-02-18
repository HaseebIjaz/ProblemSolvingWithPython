class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            # If smallest number in sorted array is greater than zero then the 3sum will never be equal to 0
            if num > 0:
                break

            # The duplicate is always the second or third one and never the first one
            # for nums[i - 1] , i must be greater than zero
            # so it caters for both the cases
            #skipping duplicates
            if i > 0 and  num == nums[i - 1]:
                continue
            
            #If we reach this part then it means that we have selected one number which is num 
            # and have skipped all its duplicated and now we will select next two nums via twoSum in the nextRange
            # out of 3 nums we have found 1 number, this is the underlying assumption

            l, r = i+1, len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]])
                    #Now next part is to prepare for the next iteration
                    
            

        
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        nums.sort()

        # if we do not sort we wont be able to generate duplicates, by sorting we will be able to generate duplicates
        # if we generate duplicates then we will be able to filter them using set

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i]+nums[j]+nums[k]:
                        tmp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(tmp))
        return [list(tup) for tup in res]
