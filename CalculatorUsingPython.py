num1 = float(input("Enter the first number :"))
num2 = float(input("Enter the second number :"))

print("Enter the number to choose the operator:")
print("1 : +")
print("2 : -")
print("3 : *")
print("4 : /")
print("5 : //")
print("6 : %")
print("7 : power(**)")
op = int(input("Enter number :"))

if op==1:
    result = num1+num2
elif op==2:
    result = num1-num2
elif op==3:
    result = num1*num2
elif op==4:
    result = num1/num2
elif op==5:
    result = num1//num2
elif op==6:
    result = num1%num2
elif op==7:
    result = num1**num2
else:
    result = "Invalid"
print("Your result is ",result)