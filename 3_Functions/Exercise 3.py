a = 85

def get_grade(a):
    if a >= 90:
        return "A"
    elif a >= 80:
        return "B"
    elif a >= 70:
        return "C"
    elif a < 70:
        return "F"

print(get_grade(a))
