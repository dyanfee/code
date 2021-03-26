#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_num = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            max_num = max(nums[i], max_num)
        return max_num
# @lc code=end
