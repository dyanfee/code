#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return str(1)
        s = self.countAndSay(n-1)
        count = 1
        res = ''
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count += 1
            else:
                res += str(count) + s[i]
                count = 1
        res += str(count) + s[len(s)-1]
        return res
# @lc code=end
