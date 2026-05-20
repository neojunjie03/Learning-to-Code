def get_number():
    while True:
        try: 
            number = int(input("Enter a number: "))
            return number
        except ValueError:
            print("That's not a number, try again!")

result = get_number()
print(f"You entered: {result}")