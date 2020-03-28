def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    ans = []
    temp = []
    for n in arr2:
        for m in arr1:
            if n==m:
                ans.append(n)
                continue
    ans = ans + sorted(temp)
    return ans