# This is faulty Calculator

value1 = input("enter number 1\n")
operator = input("enter operand\n")
value3 = input("enter number 2\n")
calculate = value1 + operator + value3
if calculate == "45*3":
    print(555)
elif calculate == "10+10":
    print(30)
elif calculate == "40/4":
    print(100)
elif operator == "+":
    print(int(value1) + int(value3))
elif operator == "-":
    print(int(value1) - int(value3))
elif operator == "/":
    print(int(value1) / int(value3))