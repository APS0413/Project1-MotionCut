class Task:
    def __init__(self, description, due_date=None, priority=None):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        print("\nTo-Do List:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task.description} - Due: {task.due_date} Priority: {task.priority}")

        print("\nCompleted Tasks:")
        for i, task in enumerate(self.completed_tasks, 1):
            print(f"{i}. {task.description}")

    def mark_as_completed(self, task_index):
        task = self.tasks.pop(task_index)
        task.completed = True
        self.completed_tasks.append(task)
        print(f"Task '{task.description}' marked as completed!")

    def update_task(self, task_index, description=None, due_date=None, priority=None):
        task = self.tasks[task_index]
        task.description = description if description else task.description
        task.due_date = due_date if due_date else task.due_date
        task.priority = priority if priority else task.priority
        print(f"Task '{task.description}' updated!")

    def remove_task(self, task_index):
        removed_task = self.tasks.pop(task_index)
        print(f"Task '{removed_task.description}' removed from the list.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Update Task")
        print("5. Remove Task")
        print("0. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional): ")
            priority = input("Enter priority (optional): ")
            task = Task(description, due_date, priority)
            todo_list.add_task(task)

        elif choice == "2":
            todo_list.display_tasks()

        elif choice == "3":
            todo_list.display_tasks()
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            todo_list.mark_as_completed(task_index)

        elif choice == "4":
            todo_list.display_tasks()
            task_index = int(input("Enter the task number to update: ")) - 1
            description = input("Enter new description (press Enter to keep the current one): ")
            due_date = input("Enter new due date (press Enter to keep the current one): ")
            priority = input("Enter new priority (press Enter to keep the current one): ")
            todo_list.update_task(task_index, description, due_date, priority)

        elif choice == "5":
            todo_list.display_tasks()
            task_index = int(input("Enter the task number to remove: ")) - 1
            todo_list.remove_task(task_index)

        elif choice == "0":
            print("Exiting the Application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
