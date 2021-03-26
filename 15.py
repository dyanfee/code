def threeSum(nums):
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n):
        f = nums[i]
        k = n-1
        if i > 0 and f == nums[i-1]:
            continue
        for j in range(i+1, n):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            while j < k and nums[i] + nums[j] + nums[k] > 0:
                k -= 1
            if j == k:
                break
            if nums[i] + nums[j] + nums[k] == 0:
                res.append([nums[i], nums[j], nums[k]])
    return res


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
