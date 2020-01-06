#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start


class Solution:
    def romanToInt(self, s: str) -> int:
        r = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        for i in range(0, len(s)-1):
            if(r[s[i]] < r[s[i+1]]):
                res -= r[s[i]]
            else:
                res += r[s[i]]

        res += r[s[-1]]
        return res
# @lc code=end
