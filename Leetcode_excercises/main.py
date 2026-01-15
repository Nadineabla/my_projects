from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {} 
        for i, n in enumerate(nums):
            complement = target - n
            if complement in store :
                return [store[complement],i]
            store[n] = i
            
result= Solution().twoSum([2,8,6,4,7,11,15],9)
print(result)