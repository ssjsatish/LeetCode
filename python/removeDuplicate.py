class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        temp = []
        for n in arr2:
            for m in arr1:
                if n==m and m not in ans:
                    ans.append(n)
                else:
                    temp.append(m)
        ans = ans + sorted(temp)
        return ans