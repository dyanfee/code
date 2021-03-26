def letterCombinations(digits: str):
    m = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
         "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    res = []
    if not len(digits):
        return []
    t = []

    def trackback(s, digits):
        if len(digits) == 0:
            return res.append(s)
        else:
            cur = digits[0]
            for each in m[cur]:
                # tmp = s + each
                trackback(s + each, digits[1:])
            # digits = digits[1:]
    trackback("", digits)
    return res


digits = "234"

print(letterCombinations(digits))
