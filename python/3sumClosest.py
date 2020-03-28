def threeSumClosest(nums, target):
    result = nums[0] + nums[1] + nums[len(nums)-1]
    nums.sort()
    for i in range(len(nums)-2):
        start = i + 1
        end = len(nums) - 1
        while start < end:
            current_sum = nums[i] + nums[start] + nums[end]
            if current_sum > target:
                end = end - 1
            else:
                start = start + 1
            if abs(current_sum -target) < abs(result - target):
                result = current_sum
    return result
