def show():
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Exit")

def add(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")
def view(tasks):
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i in tasks:
            print(i)
def completed(tasks):
    view(tasks)
    ti = int(input("Enter the task number to mark as completed: ")) - 1
    if ti < 0 or ti >= len(tasks):
        print("Invalid task number.")
    else:
        tasks.pop(ti)
        print("Task marked as completed.")

def main():
    tasks = []
    while True:
        show()
        ch = input("Enter your choice: ")
        if ch == "1":
            add(tasks)
        elif ch == "2":
            view(tasks)
        elif ch == "3":
            completed(tasks)
        elif ch == "4":
            print("Exit")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
