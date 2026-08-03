class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            vals = 1
            for j in range(len(nums)):
                if j != i:
                    vals = nums[j] * vals
                else:
                    continue
            res.append(vals)
        return res