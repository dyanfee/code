def fourSum(nums, target):
    nums.sort()
    lens = len(nums)
    res = []
    if lens < 4:
        return []
    for i in range(lens):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, lens):
            if i < j and nums[j] == nums[j-1]:
                continue
            k, l = j + 1, lens-1
            while k < l:
                s = nums[i] + nums[j] + nums[k] + nums[l]
                if s == target:
                    res.append([nums[i], nums[j], nums[k], nums[l]])
                    while k < l and nums[k] == nums[k+1]:
                        k += 1
                    while k < l and nums[l] == nums[l-1]:
                        l -= 1
                    k += 1
                    l -= 1
                else:
                    if s < target:
                        k += 1
                    else:
                        l -= 1
    return res


nums = [-3, -2, -1, 0, 0, 1, 2, 3]
target = 0
print(fourSum(nums, target))
# [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],
# [-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
