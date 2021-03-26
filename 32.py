def longestValidParentheses(s: str) -> int:
    lens = len(s)
    res = 0
    d = [0]*lens
    for i in range(lens):
        if s[i] == ")":
            if i > 0 and s[i-1] == "(":
                d[i] = (d[i-2] if i > 2 else 0) + 2
                # if i >= 2:
                #     d[i] = d[i-2]+2
                # else:
                #     d[i] = 2
            elif i-d[i-1] > 0 and s[i-d[i-1]-1] == "(":
                d[i] = d[i-1] + (d[i-d[i-1]-2] if i-d[i-1] > 2 else 0) + 2
                # d[i] = d[i-1]+2
                # if i-d[i-1] > 2:
                #     d[i] += d[i-d[i-1]-2]
        res = max(res, d[i])
    return res


s = "(()))())("
print(longestValidParentheses(s))
