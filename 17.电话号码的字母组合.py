#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
             "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        if not len(digits):
            return []

        def btrack(s, digits):
            if len(digits) == 0:
                return res.append(s)
            else:
                cur = digits[0]
                for each in m[cur]:
                    btrack(s + each, digits[1:])
        btrack("", digits)
        return res
# @lc code=end
