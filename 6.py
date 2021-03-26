s = "PAYPALISHIRING"
numRows = 1


def convert(s, numRows):
    dic = [""]*numRows
    p = -1
    flag = 1
    n = numRows - 1
    if n == 0:
        return print(s)
    for i in range(len(s)):
        if p == 0:
            flag = 1
        elif p == n:
            flag = 0
        if flag:
            p += 1
        else:
            p -= 1
        dic[p] += s[i]
    print("".join(dic))
    print(dic)


convert(s, numRows)
