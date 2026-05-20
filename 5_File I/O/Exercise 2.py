with open("notes.txt", "a") as file:
    file.write("\nI am adding one more line")
    file.write("\nI am adding one last line")

with open("notes.txt", "r") as file:
    content = file.read()
    print(content)