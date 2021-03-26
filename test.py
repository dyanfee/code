class S:
    get_n = 5
    def get(self):
        self.get_n = 10
        return self.get_n
    def get2(self):
        return self.get_n

s = S()
print(s.get())
print(s.get2())