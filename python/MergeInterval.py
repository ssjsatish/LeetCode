from operator import itemgetter
class MergeInterval:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        if len(intervals)==0:
            return ans
        intervals.sort(key=itemgetter(0))
        
        ans.append(intervals[0])
        j = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] <= ans[j][1]:
                ans[j][1] = max(intervals[i][1], ans[j][1])
            else:
                ans.append(intervals[i])
                j += 1
        return ans