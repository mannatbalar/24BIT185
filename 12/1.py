class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def add(self, c2):
        resr = self.r + c2.r
        resi = self.i + c2.i
        return (f"{resr}+ {resi}i")

    def sub(self, c2):
        resr = self.r - c2.r
        resi = self.i - c2.i
        return (f"{resr}+ {resi}i")
        

    def mul(self, c2):
        resr = self.r * c2.r - self.i * c2.i
        resi= self.r * c2.i + self.i * c2.r
        return (f"{resr}+ {resi}i")

    def div(self, c2):
        den = c2.r ** 2 + c2.i ** 2
        resr = (self.r * c2.r + self.i * c2.i) / den
        resi = (self.i * c2.r - self.r * c2.i) / den
        return (f"{resr}+ {resi}i")



c1 = Complex(4, 5)
c2 = Complex(2, 3)
 
print(c1.add(c2))
print(c1.sub(c2))
print(c1.mul(c2))
print(c1.div(c2))
