# =========================
# To-Do List CLI Application
# Beginner Friendly Python Project
# =========================

tasks = []

def show_menu():
    print("\n====== TO-DO LIST MENU ======")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
    print("=============================")

while True:
    show_menu()

    choice = input("Enter your choice (1-4): ")

    # View Tasks
    if choice == "1":
        if len(tasks) == 0:
            print("\nNo tasks available.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    # Add Task
    elif choice == "2":
        task = input("Enter a new task: ")

        if task.strip() == "":
            print("Task cannot be empty.")
        else:
            tasks.append(task)
            print(f'"{task}" added successfully!')

    # Delete Task
    elif choice == "3":
        if len(tasks) == 0:
            print("\nNo tasks to delete.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            try:
                task_number = int(input("Enter task number to delete: "))

                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f'"{removed_task}" deleted successfully!')
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    # Exit Program
    elif choice == "4":
        print("Exiting To-Do List App...")
        print("Goodbye!")
        break

    # Invalid Choice
    else:
        print("Invalid choice. Please select between 1 and 4.")
