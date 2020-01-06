#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        for i in range(0, int(len(s)*.5)):
            if(s[i] != s[len(s)-i-1]):
                return False

        return True

# @lc code=end
