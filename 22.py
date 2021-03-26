def generateParenthesis(n: int):
    res = []

    def btrack(s, left, right):
        if left == 0 and right == 0:
            res.append(s)
        if left > 0:
            btrack(s+"(", left-1, right)
        if right > 0 and left < right:
            btrack(s + ")", left, right-1)
    btrack("", n, n)

    return res


n = 3
print(generateParenthesis(n))
