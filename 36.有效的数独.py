#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dic = [{} for i in range(9)]
        col_dic = [{} for i in range(9)]
        box_dic = [{} for i in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    num = int(num)
                    b_idx = i//3 * 3 + j//3

                    row_dic[i][num] = row_dic[i].get(num, 0) + 1
                    col_dic[j][num] = col_dic[j].get(num, 0) + 1
                    box_dic[b_idx][num] = box_dic[b_idx].get(num, 0)+1

                    if row_dic[i][num] > 1 or col_dic[j][num] > 1 or box_dic[b_idx][num] > 1:
                        return False
        return True
# @lc code=end
