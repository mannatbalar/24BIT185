def fun():
    print("This is fun()")

def disp():
    print("This is disp()")

def msg():
    print("This is msg()")

functions = [fun, disp, msg]

for func in functions:
    func()