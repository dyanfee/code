#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
MIN = -2**31
MAX = 2**31 - 1


class Solution:

    def myAtoi(self, s: str) -> int:
        signed = 0
        state = 0
        num = 0
        for i in s:
            if i == ' ' and signed == 0 and state == 0:
                continue
            elif i == '-':
                if signed != 0 or state !=0:
                    break
                signed = -1
            elif i == "+":
                if signed != 0 or state !=0:
                    break
                signed = 1
            elif i.isdigit():
                state = 1
                num = num * 10 + int(i)
            else:
                break
        if signed != 0:
            num *= signed
        return self.check(num)
    
    def check(self,n):
        if n >= 0:
            return min(n, MAX)
        else:
            return max(n, MIN)



            

# @lc code=end

