def read_file(filename):
    try:
        with open(filename, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found!")

read_file("notes.txt")
read_file("missing.txt")