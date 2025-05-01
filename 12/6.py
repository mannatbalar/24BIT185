class Date:
    def __init__(self, d, m, y):
        self.y = y
        self.m = m
        self.d = d

    def __eq__(self, c2):
        return self.y == c2.y and self.m == c2.m and self.d == c2.d



d1 = Date(22, 4, 2025)
d2 = Date(22, 4, 2025)
d3 = Date(23, 4, 2025)

print(d1 == d2)
print(d1 == d3)
