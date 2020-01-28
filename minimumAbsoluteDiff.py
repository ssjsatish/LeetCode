def minimumAbsDiff(a):
    a.sort()
    minDiff = float('inf')
    for i in range(len(a)-1):
        minDiff = min(minDiff, a[i+1] - a[i])
    ans = []
    for i in range(len(a) - 1):
        if minDiff == (a[i+1]-a[i]):
            ans.append([a[i], a[i+1]])
    return ans
