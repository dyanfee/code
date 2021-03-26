#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # max = 0
        # w = 0
        # h = 0
        # length = len(height)
        # for i in range(0, length):
        #     for j in range(i+1, length):
        #         w = j-i
        #         h = height[i] if height[i] < height[j] else height[j]
        #         tmp = w*h
        #         if max < tmp:
        #             max = tmp
        # print(max)
        # return max
        m = 0
        l, r = 0, len(height)-1
        while l < r:
            h = height[l] if height[l] < height[r] else height[r]
            tmp = h * (r - l)
            if tmp > m:
                m = tmp
            # m = max(tmp,m)
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
        return m
# @lc code=end
