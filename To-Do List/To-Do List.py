import os

class TodoList:
    def __init__(self, filename="todo.txt"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Loads tasks from the file."""
        tasks = []
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        parts = line.split('|')
                        task_name = parts[0]
                        completed = parts[1].lower() == 'true' if len(parts) > 1 else False
                        tasks.append({"task": task_name, "completed": completed})
        return tasks

    def save_tasks(self):
        """Saves tasks to the file."""
        with open(self.filename, 'w') as f:
            for task_info in self.tasks:
                f.write(f'{task_info["task"]}|{task_info["completed"]}\n')

    def add_task(self, task):
        """Adds a new task to the list."""
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()
        print(f"Task '{task}' added. ✔️") 

    def view_tasks(self):
        """Displays all tasks."""
        if not self.tasks:
            print("No tasks in the list. ❌")
            return

        print("\n➖➖➖ Your To-Do List ⭐ ➖➖➖")
        for i, task_info in enumerate(self.tasks):
            status = "[X]" if task_info["completed"] else "[ ]"
            print(f"{i + 1}. {status} {task_info['task']}")
        print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")

    def mark_task_complete(self, task_number):
        """Marks a task as complete."""
        # Corrected 'self.task' to 'self.tasks'
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            self.save_tasks() 
            print(f"Task {task_number} marked as complete. ✅")
        else:
            print("Invalid task number. 👎❌")

    def delete_task(self, task_number):
        """Deletes a task from the list."""
        if 1 <= task_number <= len(self.tasks):
            deleted_task = self.tasks.pop(task_number - 1)
            self.save_tasks()
            
            print(f"Task '{deleted_task['task']}' deleted. 🗑️") 
        else:
            print("Invalid task number. 👎❌") 

def main():
    todo_list = TodoList()

    while True:
        print("\n➖➖➖ Your To-Do List ⭐ ➖➖➖")
        print("1. View tasks 🔍")
        print("2. Add tasks ➕")
        print("3. Mark task as completed ✅")
        print("4. Delete task 💀")
        print("5. Exit 🚩")
        print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")

        choice = input("Enter your choice: ")

        if choice == "1":
            todo_list.view_tasks()
        elif choice == "2":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "3":
            try:
                task_num = int(input("Enter the task number to mark as complete ✅: "))
                todo_list.mark_task_complete(task_num)
            except ValueError:
                print("Invalid input. Please enter a number. ❌")
        elif choice == "4":
            try:
                task_num = int(input("Enter the task number to delete 💀: "))
                todo_list.delete_task(task_num)
            except ValueError:
                print("Invalid input. Please enter a number. ❌")
        elif choice == "5":
            print("Exiting To-Do List. Goodbye! 👋") # Simplified emoji
            break
        else:
            print("Invalid choice. Please try again. ❌")


if __name__ == "__main__":
    main()