# 暴力解法
def largestRectangleArea1(heights) -> int:
    res = 0
    n = len(heights)
    for i, h in enumerate(heights):
        j = k = i
        while j-1 >= 0 and heights[j-1] >= h:
            j -= 1
        while k+1 <= n-1 and heights[k+1] >= h:
            k += 1
        res = max(res, h*(k-j+1))
    return res
# 单调栈
def largestRectangleArea2(heights) -> int:
    pass
s = [2, 1, 5, 6, 2, 3]
# print(largestRectangleArea1(s))
