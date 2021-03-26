
# class Match:
# str_pos = 0
# search_str = ""
# str_len = 0
# pro_str = ""
# nex_str = ""

# def isMatch(self, s: str, p: str) -> bool:
#     self.str_pos = 0
#     self.search_str = p
#     self.str_len = len(p)
#     self.pro_str = p[0] if self.str_len > 0 else ''
#     self.nex_str = p[1] if self.str_len > 1 else ''
#     for i in s:
#         if not self.search(i, self.search_str ):
#             return False
#     return True

# def search(self, i, p):
#     if i == self.pro_str or self.pro_str == ".":
#         if self.nex_str:
#             if self.nex_str != "*":
#                 self.str_pos += 1
#                 self.pro_str = self.nex_str
#                 self.nex_str = p[self.str_pos +
#                                  1] if self.str_len > self.str_pos+1 else ''
#         else:
#             self.pro_str = ""
#         return True
#     else:
#         if self.nex_str:
#             if self.nex_str == "*":
#                 self.str_pos += 2
#                 self.pro_str = p[self.str_pos] if self.str_len > self.str_pos else ''
#                 self.nex_str = p[self.str_pos +
#                                  1] if self.str_len > self.str_pos+1 else ''
#                 return self.search(i, p)
#         else:
#             return False


class Match:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        f = [[False]*(n+1) for _ in range(m+1)]
        f[0][0] = True
        for i in range(m+1):
            for j in range(1, n+1):
                if p[j-1] == "*":
                    f[i][j] = f[i][j-2]
                    if self.match(i, j-1, s, p):
                        f[i][j] = f[i-1][j] | f[i][j-2]
                else:
                    if self.match(i, j, s, p):
                        f[i][j] = f[i-1][j-1]
        print(f)
        return f[m][n]

    def match(self, i, j, s, p):
        if i == 0:
            return False
        return p[j-1] == "." or s[i-1] == p[j-1]


s = "aaa"
p = "b*a*c*a"

t = Match()
print(t.isMatch(s, p))
