from task_manager import add_task, view_tasks, complete_task, delete_task
from file_handler import load_tasks, save_tasks
from menu import menu

def main():
    tasks = load_tasks()

    while True:
        menu()
        choice = input("\nChoose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()