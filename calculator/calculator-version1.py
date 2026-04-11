num1 = float(input("enter first number: "))
operator = input("enter operator (+, -, *, /): ")
num2 = float(input("enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        result = "error: division by zero"
    else:
        result = num1 / num2
else:
    result = "invalid operator"

print("result:", result)
