#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while l < r:
            m = l + (r - l)//2
            if nums[m] > target:
                r = m
            elif nums[m] < target:
                l = m+1
            else:
                return m
        return l


# @lc code=end
