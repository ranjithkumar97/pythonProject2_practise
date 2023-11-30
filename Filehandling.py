#USE THE HIGHER ORDER FUNCTION
def add(x=3,y=5):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def funAs(funAsPara):
    print("Here is the Result")
    print(funAsPara(),add)
funAs(add)
