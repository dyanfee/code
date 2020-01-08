#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        s = len(haystack)
        n = len(needle)
        for i in range(0, s):
            if i+n > s:
                break
            for j in range(0, n):
                if i+j >= s or haystack[i+j] != needle[j]:
                    break
            else:
                return i
        return -1
# @lc code=end
