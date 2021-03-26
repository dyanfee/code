#
# @lc app=leetcode.cn id=1309 lang=python3
#
# [1309] 解码字母到整数映射
#

# @lc code=start
class Solution:
    def freqAlphabets(self, s: str) -> str:
        p = 0
        res = ""
        l = s.split("#")
        for each in l:
            if int(each)>10:
                temp = each.split("")
                for j in temp:
                    res += chr(96+int(j))
            else:
                res += chr(96+int(each))
        return res# @lc code=end

