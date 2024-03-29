#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        for i, h in enumerate(heights):
            if not stack or stack[-1]<=h:
                stack.append(h)
            
# @lc code=end
