with open("notes.txt", "w") as file:
    file.write("Hello!\n")
    file.write("I am JJ\n")
    file.write("How are you?")

with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
