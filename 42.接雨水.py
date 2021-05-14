#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        lMax = 0
        rMax = 0
        s = 0
        while left < right:
            if height[left] > lMax:
                lMax = height[left]
            if height[right] > rMax:
                rMax = height[right]
            if height[left] > height[right]:
                s += rMax-height[right]
                right -= 1
                continue
            else:
                s += lMax-height[left]
                left += 1
                continue
        return s
# @lc code=end
