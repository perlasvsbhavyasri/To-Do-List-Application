import json
import os

file_name = "tasks.json"


def load_tasks():
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    return []


def save_tasks(task_list):
    with open(file_name, "w") as file:
        json.dump(task_list, file, indent=4)


def add_task(task_list):
    print("
Add New Task")
    task_name = input("Enter task: ")
    if task_name == "":
        print("Task cannot be empty.")
        return
    task_list.append(task_name)
    save_tasks(task_list)
    print("Task added successfully.")


def view_tasks(task_list):
    print("
Your Tasks")
    if len(task_list) == 0:
        print("No tasks available.")
    else:
        number = 1
        for task in task_list:
            print(str(number) + ". " + task)
            number = number + 1


def delete_task(task_list):
    view_tasks(task_list)
    if len(task_list) == 0:
        return
    try:
        number = int(input("Enter task number to delete: "))
        if number >= 1 and number <= len(task_list):
            removed_task = task_list.pop(number - 1)
            save_tasks(task_list)
            print("Deleted task:", removed_task)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter only a number.")


def clear_tasks(task_list):
    confirm = input("Do you want to clear all tasks? (yes/no): ")
    if confirm.lower() == "yes":
        task_list.clear()
        save_tasks(task_list)
        print("All tasks cleared.")
    else:
        print("Clear operation cancelled.")


def show_menu():
    task_list = load_tasks()

    while True:
        print("
===== TO-DO LIST APPLICATION =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Clear All Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(task_list)
        elif choice == "2":
            view_tasks(task_list)
        elif choice == "3":
            delete_task(task_list)
        elif choice == "4":
            clear_tasks(task_list)
        elif choice == "5":
            print("Thank you")
            break
        else:
            print("Please enter a number from 1 to 5.")


show_menu()
