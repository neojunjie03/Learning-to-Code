with open("todo.txt", "w") as file:
    file.write("1. Buy groceries\n")
    file.write("2. Do laundry\n")
    file.write("3. Study Python")

def add_task(task):
    with open("todo.txt", "a") as file:
        file.write(f"\n{task}")
    
def show_tasks():
    with open("todo.txt", "r") as file:
        print(file.read())

add_task("4. Clean room")
add_task("5. Shower")
add_task("6. Sleep")
show_tasks()