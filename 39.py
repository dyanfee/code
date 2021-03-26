# 给定一个无重复元素的数组 candidates 和一个目标数
# target ，找出 candidates 中所有可以使数字和为
# target 的组合。
# candidates 中的数字可以无限制重复被选取。

# 输入：candidates = [2,3,6,7], target = 7,
# 所求解集为：
# [
#   [7],
#   [2,2,3]
# ]


def combinationSum(candidates, target: int):

    res = []
    lens = len(candidates)

    def btrack(target, curList: list, pos):

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


s = [2, 3, 6, 7]
target = 7
# print(combinationSum(s, target))


def combinationSum2(candidates, target: int):
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


s = [2, 5, 2, 1, 2, 2]
target = 5
print(combinationSum2(s, target))
