class solid:
    def __init__(self,l,b,h):
        self.l = l
        self.b = b
        self.h = h

    def sa(self):
        sa = 2*((self.l*self.h)+(self.l*self.b)+(self.b*self.h))
        return sa
    def vol(self):
        vol = (self.l)*(self.b)*(self.h)
        return vol
    

dim = solid(10,10,10)

print(dim.sa())
print(dim.vol())