MIN = -2**31
MAX = 2**31 - 1


def myAtoi(s: str) -> int:
    signed = 0
    num = 0
    for i in s:
        if i == ' ':
            continue
        elif i == '-':
            if signed != 0:
                break
            signed = -1
        elif i == "+":
            if signed != 0:
                break
            signed = 1
        elif i.isdigit():
            num = num * 10 + int(i)
        else:
            break
    if signed != 0:
        num *= signed
    print(check(num))


def check(n):
    if n >= 0:
        return min(n, MAX)
    else:
        return max(n, MIN)


# s = "42"
# s = "   +42"
# s = "4193 with words"
# s = "words and 987"
s = "-91283472332"

myAtoi(s)
