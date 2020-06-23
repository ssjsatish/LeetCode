class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [(start+2*i) for i in range(n)]
        xor_arr = 0
        for i in range(len(nums)):
            xor_arr = xor_arr ^ nums[i] 
        return xor_arr