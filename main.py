from datetime import datetime
import json


commands = {
    "add \"<task>\"": "Adds a new task",
    "update <id> \"<task>\"": "Updates a task",
    "delete <id>": "Deletes a task",
    "mark-in-progress <id>": "Marks a task as in progress",
    "mark-done <id>": "Marks a task as done",
    "list": "Lists all tasks",
    "list done/todo/in-progress": "Lists tasks by status",
}


def printCommands(commands):
    for key, value in commands.items():
        print(f"{key:<30} {value}")
def printListLikeTable(tasks):
    longest_task_length = max(len(t['task']) for t in tasks) if tasks else 0
    task_column_width = max(longest_task_length, len("Task")) + 2
    print(f"{'ID':<5} {'Task':<{task_column_width}} {'Status':<13} {'Created At':<20} {'Updated At':<20}")
    print("-" * (task_column_width + 60))
    for t in tasks:
        print(f"{t['id']:<5} {t['task']:<{task_column_width}} {t['status']:<13} {t['created_at']:<20} {t['updated_at']:<20}")
    print("-" * (task_column_width + 60))

def initialize_tasks_file():
    try:
        with open("tasks.json", "r") as file:
            json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        with open("tasks.json", "w") as file:
            json.dump([], file)
initialize_tasks_file()
print("=" * 70)
print("Welcome to the Task Tracker CLI v1.0!".center(70))

while True:
    print("=" * 70)
    command = input("task-cli %  ").strip()
    if command == "exit":
        print()
        print("Exiting the Task Tracker CLI. Goodbye!")
        break
    elif command == "help":
        print()
        printCommands(commands)
    elif command.startswith("add "):
        print()
        print("Adding a new task...")
        # task = command[5:-1].strip()
        parts = command.split(" ", 1)
        if parts[1].startswith('"') and parts[1].endswith('"'):
            task = parts[1][1:-1].strip()
            # Add task logic here
            with open("tasks.json", "r+") as file:
                tasks = json.load(file)
                new_task = {
                    "id": len(tasks) + 1,
                    "task": task,
                    "status": "todo",
                    "created_at": datetime.now().strftime("%m/%d/%y %I:%M %p"),
                    "updated_at": "not updated yet"
                }
                tasks.append(new_task)
                file.seek(0)
                json.dump(tasks, file, indent=4)
            print(f"Output: Task added successfully (ID: {new_task['id']})")
        else:
            print("Invalid command format. Please use: add \"<task>\"")
    elif command.startswith("update ") or command.startswith("delete "):
        print()
        parts = command.split(" ", 2) 
        if len(parts) == 3 and command.startswith("update ") and parts[2].startswith('"') and parts[2].endswith('"'):
            task_id, task = parts[1], parts[2][1:-1].strip()
            with open("tasks.json", "r+") as file:
                tasks = json.load(file)
                for t in tasks:
                    if str(t["id"]) == task_id:
                        t["task"] = task
                        t["updated_at"] = datetime.now().strftime("%m/%d/%y %I:%M %p")
                        break
                file.seek(0)
                json.dump(tasks, file, indent=4)
                file.truncate()
            print(f"Task {task_id} updated to: {task}")
        elif len(parts) == 2 and command.startswith("delete "):
            task_id = parts[1]
            with open("tasks.json", "r+") as file:
                tasks = json.load(file)
                tasks = [t for t in tasks if str(t["id"]) != task_id]
                file.seek(0)
                json.dump(tasks, file, indent=4)
                file.truncate()
            print(f"Task {task_id} deleted successfully.")
        else:
            print("Invalid command format. Please use: update <id> \"<task>\" or delete <id>")  
    elif command.startswith("mark-in-progress ") or command.startswith("mark-done "):
        print()
        parts = command.split(" ", 1)
        status, task_id = ' '.join(parts[0].split("-")[1:]), parts[1]
        with open("tasks.json", "r+") as file:
            tasks = json.load(file)
            for t in tasks:
                if str(t["id"]) == task_id:
                    t["status"] = status
                    t["updated_at"] = datetime.now().strftime("%m/%d/%y %I:%M %p")
                    break
            file.seek(0)
            json.dump(tasks, file, indent=4)
            file.truncate()
        print(f"Task {task_id} marked as \"{status}\".")
    elif command == "list":
        print()
        # List all tasks logic here
        print("Listing all tasks...")
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            printListLikeTable(tasks)
    elif command.startswith("list "):
        print()
        status = ' '.join(command.split(" ")[1:]).strip()
        # List tasks by status logic here
        print(f"Listing tasks with status: {status}")
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            filtered_tasks = [t for t in tasks if t["status"] == status]
            if not filtered_tasks:
                print(f"No tasks found with status: {status}")
            else:
                printListLikeTable(filtered_tasks)
    else:
        print()
        print("Invalid command. Please try again.")
    

