class everything:
    def __init__(self,l,b,r):
        self.b = b
        self.l = l
        self.r = r

    def sqperi(self):
        return 4*(self.l)
    
    def rectperi(self):
        return 2*(self.l + self.b)
    
    def circum(self):
        return 2*(3.14)*(self.r)
    
    def sqa(self):
        return (self.l)**2
    
    def recta(self):
        return (self.l)*(self.b)
    
    def cira(self):
        return 3.14*((self.r)**2)
    
print("Select your shape")
print("1 for square")
print("2 for rectangle")
print("3 for circle")
a = int(input("Enter your choice:"))

if a == 1:
    len = float(input("Enter the length of square: "))
    square = everything(len,0,0)
    print("Perimeter of square is:")
    print(square.sqperi())
    print("Area of square is:")
    print(square.sqa())

elif a == 2:
    len = float(input("Enter the length of rectangle: "))
    bre = float(input("Enter the breadth of rectangle: "))
    rect = everything(len,bre,0)
    print("Perimeter of rectable is:")
    print(rect.rectperi())
    print("Area of rectanle is:")
    print(rect.recta())

elif a == 3:
    rad = float(input("Enter the radius of circle: "))
    circle = everything(0,0,rad)
    print("circumference of circle is:")
    print(circle.circum())
    print("Area of circle is:")
    print(circle.cira())