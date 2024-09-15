# **To-Do List App (Command-Line Version)**

## **Overview**

This **To-Do List App** is a simple command-line Python project designed to help users manage tasks. The app allows you to add tasks, view them, mark them as complete, and delete them. It also saves tasks to a file so that they persist between sessions.

### **Features**
- Add tasks with descriptions
- View all tasks, including their completion status
- Mark tasks as complete
- Delete tasks
- Save and load tasks to/from a JSON file

---

## **Project Structure**

```
todo_list_app/
│
├── main.py                 # Entry point for the app
├── task_manager.py         # Handles task operations (add, view, mark complete, delete)
├── file_handler.py         # Manages saving and loading tasks to/from a file
└── menu.py                 # Displays menu options and handles user interaction
```

### **File Breakdown**

1. **`main.py`**
   - The main entry point of the app. It contains the main loop and orchestrates the flow of the application.
   
2. **`task_manager.py`**
   - Contains functions for managing tasks such as adding, viewing, marking as complete, and deleting tasks.
   
3. **`file_handler.py`**
   - Manages loading tasks from a JSON file and saving the updated tasks back to the file, ensuring task persistence.
   
4. **`menu.py`**
   - Displays the menu and provides the user interface for choosing options like viewing tasks, adding tasks, etc.

---

## **Setup Instructions**

### **1. Prerequisites**
- **Python 3.x** installed on your system. You can download it from [here](https://www.python.org/downloads/).

### **2. Clone the Repository**
You can clone the repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/todo-list-app.git
cd todo_list_app
```

Or create the project structure manually and copy the provided code.

### **3. Run the App**

1. Navigate to the project directory where you have the `main.py` file.

2. Run the following command to start the app:

```bash
python main.py
```

---

## **How to Use**

Once the app is running, you will see a menu with the following options:

```
--- To-Do List App ---
1. View Tasks
2. Add a Task
3. Mark Task as Complete
4. Delete a Task
5. Exit
```

### **1. View Tasks**
- Select option `1` to view all tasks. The tasks will be displayed in a numbered list with their completion status:
  - `[✔]` for completed tasks
  - `[ ]` for incomplete tasks

### **2. Add a Task**
- Select option `2` to add a new task.
- You will be prompted to enter a task description, and it will be added to the list as incomplete.

### **3. Mark Task as Complete**
- Select option `3` to mark a task as complete.
- You will be shown a list of tasks, and you can enter the task number to mark it as complete.

### **4. Delete a Task**
- Select option `4` to delete a task.
- You will be shown a list of tasks, and you can enter the task number to delete it.

### **5. Exit**
- Select option `5` to exit the application.

---

## **File Handling**
- The tasks are saved in a JSON file named `tasks.json` in the same directory as the script.
- Each time you add, complete, or delete a task, the changes are automatically saved to this file.
- When you restart the app, it will load tasks from the `tasks.json` file, so your progress is never lost.

---

## **Project Modules**

### **1. `task_manager.py`**
Handles all task-related operations:
- **`add_task(tasks)`**: Prompts the user to enter a new task and adds it to the list.
- **`view_tasks(tasks)`**: Displays all tasks with their status (complete or incomplete).
- **`complete_task(tasks)`**: Marks a selected task as complete.
- **`delete_task(tasks)`**: Deletes a selected task from the list.

### **2. `file_handler.py`**
Manages loading and saving tasks to a JSON file:
- **`load_tasks(filename)`**: Loads tasks from the JSON file. If the file doesn't exist, it returns an empty list.
- **`save_tasks(tasks, filename)`**: Saves the current tasks to the JSON file, ensuring task persistence.

### **3. `menu.py`**
Displays the menu and handles user interaction:
- **`menu()`**: Displays the menu options to the user and prompts for input.

---

## **Future Enhancements**

- Add task categories (e.g., Personal, Work).
- Implement task deadlines with date and time.
- Allow users to edit tasks.
- Improve error handling and input validation.

---

## **Contributing**

If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. Contributions are welcome!

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **Contact**

If you have any questions or need further assistance, feel free to contact me:

- Name: Goodness James Akoma
- Email: your-email@example.com (update with your actual contact info)
- GitHub: [your-github-profile](https://github.com/your-username)
