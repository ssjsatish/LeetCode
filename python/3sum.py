class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        instances = {}
        for n in nums:
            if n in instances:
                count = instances[n]
                if count == 1 or (n == 0 and count == 2):
                    instances[n] += 1
            else:
                instances[n] = 1        
        for n, count in instances.iteritems():
            if count == 2 and (n == 0 or -2 * n not in instances):
                instances[n] = 1
        
        #create an ordered list of values
        values = []
        for n, count in sorted(instances.iteritems()):
            for i in range(count):
                values.append(n)
        nvalues = len(values)
        while nvalues >= 4:
            floor = -(values[nvalues-1] + values[nvalues-2])
            ceiling = -(values[0] + values[1])
            if floor > ceiling:
                return []
            iLeft = nvalues
            iRight = -1
            for i in range(nvalues):
                if values[i] >= floor:
                    iLeft = i
                    break
            for i in range(nvalues-1, -1, -1):
                if values[i] <= ceiling:
                    iRight = i
                    break
            if iLeft == 0 and iRight == nvalues - 1:
                break
            values = values[iLeft:iRight+1]
            nvalues = len(values)
        if nvalues < 3:
            return []
            
        result = []
        #special case for (0,0,0), otherwise v1 must be negative
        if 0 in instances and instances[0] == 3:
            result.append([0,0,0])
        for i in range(nvalues-2):
            v1 = values[i]
            if v1 >= 0:
                break
            if i > 0 and v1 == values[i-1]:
                continue
            for j in range(i+1,nvalues-1):
                v2 = values[j]
                if j > i+1 and v2 == values[j-1]:
                    continue
                v3 = -(v1 + v2)
                if v3 < v2:
                    break
                if v3 in instances:
                    if v3 > v2 or instances[v3] > 1:
                        result.append([v1,v2,v3])
        return result

    def threeSumAlt(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if i>0 and nums[i-1]==nums[i]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                sums = nums[i]+nums[left]+nums[right]
                if sums == 0:
                    ans.append([nums[i],nums[left],nums[right]])
                    while left< right and nums[left]==nums[left+1]:
                        left +=1
                    while left < right and nums[right]==nums[right-1]:
                        right -=1
                    left +=1
                    right -=1
                elif sums>0:
                    right -=1
                elif sums<0:
                    left +=1
        return ans