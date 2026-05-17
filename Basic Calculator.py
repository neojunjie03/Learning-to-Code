num1 = input("Input first number: ")
num2 = input("Input second number: ")
operation = input("Input operation (+ - x /): ")

if operation == "+":
    print(float(num1) + float(num2)) 
elif operation == "-":
    print(float(num1) - float(num2)) 
elif operation == "x":
    print(float(num1) * float(num2)) 
elif operation == "/":
    print(float(num1) / float(num2)) 
else:
    print("Error!") 