def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
       return "Cannot divide by zero!"
    except TypeError:
        return "Please enter numbers only!"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "hi"))