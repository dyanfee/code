#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.searchNum(nums, target, True)
        right = self.searchNum(nums, target, False) - 1
        res = [-1, -1]
        if left <= right and right < len(nums) and nums[left] == target and nums[right] == target:
            res = [left, right]
        return res

    def searchNum(self, nums, target, lower):
        l, r = 0, len(nums)-1
        res = len(nums)
        while l <= r:
            mid = (l+r)//2
            if nums[mid] > target or (lower and nums[mid] >= target):
                r = mid-1
                res = mid
            else:
                l = mid + 1
        return res
# @lc code=end
