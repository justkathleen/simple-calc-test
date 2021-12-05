def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x//y
def divideround(x,y):
    return x/y

print("select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("enter choice:")
    if choice in ("1","2","3","4"):
        num1=float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))
        if choice == "1":
            print(num1,"+", num2, "=", add(num1,num2))
        if choice == "2":
            print(num1,"-", num2, "=", subtract(num1,num2))
        if choice == "3" :
                print(num1, "*", num2, "=",multiply(num1, num2))
        if choice =="4":
                print(num1, "/", num2, "=",divide(num1, num2))

else:
    print("Not valid")
