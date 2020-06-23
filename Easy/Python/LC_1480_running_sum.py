class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)-1):
            result.append(sum(nums[:i+1]))
        result.append(result[-1]+nums[-1])
        return result