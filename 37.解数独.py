#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [[False]*9 for _ in range(9)]
        cols = [[False]*9 for _ in range(9)]
        box = [[False]*9 for _ in range(9)]

        vaild = False
        waitList = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    waitList.append((i, j))
                else:
                    num = int(board[i][j])-1
                    rows[i][num] = cols[j][num] = box[i //
                                                      3 * 3 + j//3][num] = True

        def btrack(pos):
            nonlocal vaild
            if pos == len(waitList):
                vaild = True
                return
            i, j = waitList[pos]
            for n in range(9):
                if rows[i][n] == cols[j][n] == box[i//3*3+j//3][n] == False:
                    rows[i][n] = cols[j][n] = box[i//3*3+j//3][n] = True
                    board[i][j] = str(n+1)
                    btrack(pos+1)
                    rows[i][n] = cols[j][n] = box[i//3*3+j//3][n] = False
                if vaild:
                    return
        btrack(0)


# @lc code=end
