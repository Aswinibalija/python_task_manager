import json

class Task:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

    def __str__(self):
        return f"Task(id={self.id}, title='{self.title}', completed={self.completed})"

tasks = []

def add_task(title):
    id = len(tasks) + 1
    task = Task(id, title)
    tasks.append(task)
    print(f"Task '{title}' added.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    for task in tasks:
        status = "Completed" if task.completed else "Not Completed"
        print("ID: {id}, Title: {title}, Status: {status}".format(
            id=task.id, title=task.title, status=status))

def delete_task(id):
    global tasks
    tasks = [task for task in tasks if task.id != id]
    print(f"Task with ID {id} deleted.")

def mark_task_completed(id):
    for task in tasks:
        if task.id == id:
            task.completed = True
            print(f"Task with ID {id} marked as completed.")
            return
    print(f"Task with ID {id} not found.")

def save_tasks():
    with open('tasks.json', 'w') as file:
        json_tasks = [task.__dict__ for task in tasks]
        json.dump(json_tasks, file)
    print("Tasks saved.")

def load_tasks():
    global tasks
    try:
        with open('tasks.json', 'r') as file:
            json_tasks = json.load(file)
            tasks = [Task(**task) for task in json_tasks]
        print("Tasks loaded.")
    except FileNotFoundError:
        print("No saved tasks found.")

def show_menu():
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Complete")
    print("5. Save Tasks")
    print("6. Load Tasks")
    print("7. Exit")

def main():
    load_tasks()
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter task title: ")
            add_task(title)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            id = int(input("Enter task ID to delete: "))
            delete_task(id)
        elif choice == '4':
            id = int(input("Enter task ID to mark as complete: "))
            mark_task_completed(id)
        elif choice == '5':
            save_tasks()
        elif choice == '6':
            load_tasks()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
