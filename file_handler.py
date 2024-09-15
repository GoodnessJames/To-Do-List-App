import json

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as f:
            tasks = json.load(f)
        return tasks
    except FileNotFoundError:
        return []
    
def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump(tasks, f)