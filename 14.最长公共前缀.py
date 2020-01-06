#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # res = ""
        # if strs != []:
        #     for i in range(1, len(strs[0])+1):
        #         r = strs[0][0:i]
        #         for each in strs:
        #             if each[0:i] != r:
        #                 return res
        #         res = r
        # return res

        if strs == []:
            return ""
        r = list(map(set, zip(*strs)))
        res = ""
        for i, v in enumerate(r):
            if(len(r[i]) > 1):
                break
            res += list(r[i])[0]
        return res
# @lc code=end
