class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        req = 0
        for i in range (len(nums)):
            req = target - nums[i]  
            for j in range (len(nums)):
                if j != i and nums[j] ==  req:
                    return [i,j]
        