#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        lens = len(candidates)

        def btrack(target, curList, pos):

            if pos == lens:
                return
            if target == 0:
                res.append(curList)
                return

            btrack(target, curList, pos+1)

            cur = candidates[pos]
            if target - cur >= 0:
                btrack(target-cur, curList+[cur], pos)

        btrack(target, [], 0)
        return res
# @lc code=end
