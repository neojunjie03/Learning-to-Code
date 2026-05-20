def get_number():
    try: 
        a = int(input("Enter a number: "))
        print(a)
    except TypeError:
        print("That's not a number, try again!")

get_number()