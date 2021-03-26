#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start


class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        f = [[False]*(n+1) for _ in range(m+1)]
        f[0][0] = True
        for i in range(m+1):
            for j in range(1, n+1):
                if p[j-1] == "*":
                    f[i][j] = f[i][j-2]
                    if self.match(i, j-1, s, p):
                        f[i][j] = f[i-1][j] | f[i][j-2]
                else:
                    if self.match(i, j, s, p):
                        f[i][j] = f[i-1][j-1]
        return f[m][n]

    def match(self, i, j, s, p):
        if i == 0:
            return False
        return p[j-1] == "." or s[i-1] == p[j-1]
        # @lc code=end
