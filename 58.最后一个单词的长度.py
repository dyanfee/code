#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # sp = s.strip()
        # return len(sp.split()[-1]) if len(sp)>0 else 0
        return len(s.strip().split()[-1]) if len(s.strip()) > 0 else 0
# @lc code=end
