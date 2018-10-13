print("My first python program on simple calculator")
#This function adds two numbers
def add(x,y):
    return x+y

#This function do the subtraction
def sub(x,y):
    return x-y

#This function do the multiplication
def mul(x,y):
    return x*y

#This function do the division
def div(x,y):
    return x/y

print("Selection operation")
print("1 to add")
print("2 to subtract")
print("3 to mulitply")
print("4 to division")

#take input from user
choice = input("Enter choice number (1,2,3,4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter Second number: "))

if choice == "1":
    print(num1," + ",num2," = ", add(num1,num2))

elif choice == "2":
    print(num1," + ",num2," = ", sub(num1,num2))

elif choice == "3":
    print(num1," + ",num2," = ", mul(num1,num2))

elif choice == "4":
    print(num1," + ",num2," = ", div(num1,num2))
else:
    print("invalid choice")

