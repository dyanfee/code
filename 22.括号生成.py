#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def btrack(s, left, right):
            if left == 0 and right == 0:
                res.append(s)
            if left > 0:
                btrack(s+"(", left-1, right)
            if right > 0 and left < right:
                btrack(s + ")", left, right-1)
        btrack("", n, n)
        return res
# @lc code=end
