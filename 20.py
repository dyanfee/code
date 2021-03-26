def isValid(s: str) -> bool:
    c_map = {")": "(", "]": "[", "}": "{"}
    res = []
    if len(s) % 2 == 1:
        return False
    for i in s:
        if i in c_map:
            if len(res) == 0 or res[-1] != c_map[i]:
                return False
            res.pop()
        else:
            res.append(i)
    return len(res) == 0


print(isValid("()"))
