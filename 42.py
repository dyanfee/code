def trap(height) -> int:
    n = len(height)
    left = 0
    right = n-1
    lMax = 0
    rMax = 0
    s = 0
    while left < right:
        if height[left] > lMax:
            lMax = height[left]
        if height[right] > rMax:
            rMax = height[right]
        if height[left] > height[right]:
            s += rMax-height[right]
            right -= 1
            continue
        else:
            s += lMax-height[left]
            left += 1
            continue
    return s


s = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(s))
