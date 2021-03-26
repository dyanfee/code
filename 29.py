MAX = 2**31-1
MIN = -2**31


def divide(dividend: int, divisor: int) -> int:
    if dividend == 0:
        return 0
    if divisor == 1:
        return dividend
    if divisor == -1:
        return checkRes(-dividend)
    res = 0
    sign = -1
    if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
        sign = 1
    a = dividend if dividend > 0 else -dividend
    b = divisor if divisor > 0 else -divisor
    res = btrack(a, b) * sign
    return checkRes(res)


def checkRes(res):
    return MAX if res > MAX else MIN if res < MIN else res


def btrack(a, b):
    if a < b:
        return 0
    s = 1
    d = b
    while d+d < a:
        s = s + s
        d = d + d
    return s + btrack(a-d, b)


print(divide(-2147483648, -1))
