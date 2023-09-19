import json

# Define a class to represent individual tasks
class Task:
    def __init__(self, name, description, due_date):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.completed = False  # Initialize tasks as incomplete/false by default

# Define a Manager class to manage a list of tasks
class TaskManager:
    def __init__(self):
        self.tasks = []  # Initialize an empty list to store tasks

    def create_task(self, name, description, due_date):
        
        # Create a Task object and add it to the list of tasks
        task = Task(name, description, due_date)
        self.tasks.append(task)

    def list_tasks(self):

        # Display a list of tasks with their details and achievement status

        for index, task in enumerate(self.tasks, start=1):
            status = "Completed" if task.completed else "Pending"
            print(f"{index}. {task.name} ({status}) - Due Date: {task.due_date}")

    def mark_as_complete(self, task_index):

        # Mark a task as completed based on the provided task_index

        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].completed = True

    def save_tasks_to_file(self, filename):

        # Save the list of tasks to a JSON file

        with open(filename, 'w') as file:
            task_data = [{'name': task.name, 'description': task.description,
                          'due_date': task.due_date, 'completed': task.completed}
                         for task in self.tasks]
            json.dump(task_data, file)

    def load_tasks_from_file(self, filename):

        # Load tasks from a JSON file and populate the tasks list

        try:
            with open(filename, 'r') as file:
                task_data = json.load(file)
                self.tasks = [Task(task['name'], task['description'], task['due_date'])
                              for task in task_data]
        except FileNotFoundError:
            self.tasks = []  # Handle the case where the file doesn't exist

    def get_pending_tasks(self):

        # Get a list of pending tasks (tasks that are not completed)

        return list(filter(lambda task: not task.completed, self.tasks))

    def get_task_names(self):

        # Get a list of task names

        return list(map(lambda task: task.name, self.tasks))

# Define the main function to run the Task Manager application
def main():

    # Create a TaskManager instance to manage tasks
    task_manager = TaskManager()

    while True:
        print("ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.")
        print("ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.")
        print("₊˚ʚ ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.₊˚ʚ TASK MANAGER APP ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.")
        print("ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.")
        print("ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.₊˚ʚ ᗢ₊˚✧ ﾟ.")

        print("\nMenu:")
        
        print("1. Create Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete")
        print("4. Save Tasks to File")
        print("5. Load Tasks from File")
        print("6. Get Pending Tasks")
        print("7. Get Task Names")
        print("8. Quit")

        try:
            choice = input("\nEnter your choice: ")

            if choice == "1":
                name = input("\nEnter task name: ")
                description = input("Enter task description: ")
                due_date = input("Enter due date: ")
                task_manager.create_task(name, description, due_date)
                print("\nTask created successfully!\n")

            elif choice == "2":
                print("\nTask List:")
                task_manager.list_tasks()
                print("\n")

            elif choice == "3":
                task_manager.list_tasks()
                try:
                    task_index = int(input("\nEnter the task number to mark as complete: "))
                    task_manager.mark_as_complete(task_index)
                except ValueError:
                    print("\nPlease enter a valid task number.\n")

            elif choice == "4":
                filename = input("\nEnter the filename to save tasks: ")
                task_manager.save_tasks_to_file(filename)
                print(f"Tasks saved to {filename}.")

            elif choice == "5":
                filename = input("\nEnter the filename to load tasks from: ")
                task_manager.load_tasks_from_file(filename)
                print(f"Tasks loaded from {filename}.")

            elif choice == "6":
                pending_tasks = task_manager.get_pending_tasks()
                print("\nPending Tasks:")
                for index, task in enumerate(pending_tasks, start=1):
                    print(f"{index}. {task.name}")
                    print("\n")

            elif choice == "7":
                task_names = task_manager.get_task_names()
                print("\nTask Names:")
                for index, name in enumerate(task_names, start=1):
                    print(f"{index}. {name}")
                    print("\n")

            elif choice == "8":
                print("\nExiting Task Manager. bye! ૮ ˶ᵔ ᵕ ᵔ˶ ა")
                break

            else:
                print("\nPlease select a valid option.\n")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

# Run the main function 

main()
