#By using Functions mathematical Operation Performance
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
#Selecting Opeartions by Numbers
print("Please select Operation:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

a = input("Enter a(1/2/3/4):")
#Two numbers Storing in num1,num2
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))
#Calling Functions
if a == '1':
    print(num1, "+" , num2, "=" , add(num1,num2))
elif a == '2':
    print(num1, "-" , num2, "=" , sub(num1,num2))
elif a == '3':
    print(num1, "*" , num2, "=" , mul(num1,num2))
elif a == '4':
    print(num1, "/" , num2, "=" , div(num1,num2))
else:
    print("Enter The Correct Input:")
    
