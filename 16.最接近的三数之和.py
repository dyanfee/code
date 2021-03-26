#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0:3]
        dis = nums[0]+nums[1]+nums[2]
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = n-1
            while j < k:
                r = nums[i] + nums[j] + nums[k]
                if r == target:
                    return target
                if abs(r-target) < abs(dis-target):
                    dis = r
                if r < target:
                    j += 1
                else:
                    k -= 1
        return dis

# @lc code=end
