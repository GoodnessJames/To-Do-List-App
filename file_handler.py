from datetime import datetime
import json

def serialize_task(task):
    if isinstance(task["deadline"], datetime):
        task["deadline"] = task["deadline"].strftime("%Y-%m-%d %H:%M")
    return task

def deserialize_task(task):
    if "deadline" in task:
        try:
            task["deadline"] = datetime.strptime(task["deadline"], "%Y-%m-%d %H:%M")
        except (ValueError, TypeError):
            task["deadline"] = None
    return task

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as f:
            data = f.read()
            if not data.strip():
                return []
            try:
                tasks = json.loads(data)
            except json.JSONDecodeError as e:
                print(f"Failed to decode JSON: {e}")
                return []
            tasks = [deserialize_task(task) for task in tasks]
    except FileNotFoundError:
        tasks = []
    return tasks
    
def save_tasks(tasks, filename="tasks.json"):
    tasks_to_save = [serialize_task(task) for task in tasks]
    with open(filename, "w") as f:
        json.dump(tasks_to_save, f, indent=4)