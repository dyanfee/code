#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        dic = [""]*numRows
        p = -1
        flag = 1
        n = numRows - 1
        if n == 0:
            return s
        for i in range(len(s)):
            if p == 0:
                flag = 1
            elif p == n:
                flag = 0
            if flag:
                p += 1
            else:
                p -= 1
            dic[p] += s[i]
        return "".join(dic)
# @lc code=end
