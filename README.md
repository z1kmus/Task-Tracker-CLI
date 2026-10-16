# Task Tracker CLI

A simple command-line task manager written in Python. It stores tasks in a local `tasks.json` file and lets you add, update, delete, and track task progress from the terminal.

Project URL -> https://roadmap.sh/projects/task-tracker

## Features

- Add new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as `todo`, `in progress`, or `done`
- List all tasks or filter by status
- Persistent storage using JSON
- Simple interactive CLI

## Project Structure

- `main.py` — CLI application logic
- `tasks.json` — task storage file
- `.gitignore` — ignored files and directories

## Requirements

- Python 3.x

## Run the project

```bash
python main.py
```

## Available commands

```text
add "<task>"                 Adds a new task
update <id> "<task>"         Updates a task
delete <id>                  Deletes a task
mark-in-progress <id>        Marks a task as in progress
mark-done <id>               Marks a task as done
list                         Lists all tasks
list done                    Lists tasks with status "done"
list todo                    Lists tasks with status "todo"
list in-progress             Lists tasks with status "in progress"
help                         Shows command list
exit                         Exits the program
```

## Example usage

```bash
python main.py
```

Then enter commands like:

```text
task-cli %  add "Write project proposal"
task-cli %  list
task-cli %  mark-done 1
task-cli %  exit
```

## Task format

Each task is saved as an object in `tasks.json` with the following fields:

```json
{
  "id": 1,
  "task": "Write project proposal",
  "status": "todo",
  "created_at": "10/15/26 04:49 PM",
  "updated_at": "not updated yet"
}
```

## Notes

- The project uses the local JSON file as its database.
- If `tasks.json` does not exist, it is created automatically.
- `updated_at` changes when a task is modified or status is updated.

## License

This project is provided as-is for learning and personal use.

Made with ❤️ by z1kmus.
