#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = 0
        for i in range(0, len(nums)):
            if nums[s] != nums[i]:
                s += 1
                nums[s] = nums[i]
        return s+1
# @lc code=end
