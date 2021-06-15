"""Storing Values in num1 and num2"""
num1 = int(input("Enter the First integer Value:"))
num2 = int(input("Enter the Second Integer Value:"))
#Applying math operation 
print("Select Operation:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

x = input("Enter x(1/2/3/4):")

if x == '1':
    print(num1,"+",num2, "=" , num1+num2)
elif x == '2':
    print(num1,"-",num2, "=" , num1-num2)
elif x == '3':
    print(num1, "*", num2, "=" , num1*num2)
elif x == '4':
    print(num1,"/", num2 , "=", num1/num2)
else:
    print("Please Enter Correct Input Value")
