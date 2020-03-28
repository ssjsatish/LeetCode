class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for a in nums:
            ans = ans^a
        return ans