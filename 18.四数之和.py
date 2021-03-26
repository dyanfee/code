#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        lens = len(nums)
        res = []
        if lens < 4:
            return []
        for i in range(lens):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, lens):
                if i+1 < j and nums[j] == nums[j-1]:
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

# @lc code=end
