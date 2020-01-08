#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        s = 0
        for i in range(0, len(nums)):
            if(nums[i] != val):
                nums[s] = nums[i]
                s += 1
        return s
# @lc code=end
