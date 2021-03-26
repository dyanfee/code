#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        lens = len(candidates)
        candidates.sort()

        def btrack(target, curList, pos):
            if target == 0:
                res.append(curList)
                return
            for i in range(pos, lens):
                cur = candidates[i]
                if cur > target:
                    break
                if i > pos and candidates[i] == candidates[i-1]:
                    continue
                btrack(target-cur, curList+[cur], i+1)

        btrack(target, [], 0)
        return res
# @lc code=end
