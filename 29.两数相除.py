#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
MAX = 2**31-1
MIN = -2**31


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if divisor == 1:
            return self.checkRes(dividend)
        if divisor == -1:
            return self.checkRes(-dividend)
        res = 0
        sign = -1
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
        a = dividend if dividend > 0 else -dividend
        b = divisor if divisor > 0 else -divisor
        res = self.btrack(a, b) * sign
        return self.checkRes(res)

    def checkRes(self, res):
        return MAX if res > MAX else MIN if res < MIN else res

    def btrack(self, a, b):
        if a < b:
            return 0
        s = 1
        d = b
        while d+d < a:
            s = s + s
            d = d + d
        return s + self.btrack(a-d, b)
# @lc code=end
