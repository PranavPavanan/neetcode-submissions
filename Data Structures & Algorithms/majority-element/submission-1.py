class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        for i,j in freq.items():
            if j > n/2:
                return i
        return i

        