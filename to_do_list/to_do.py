import json

# Store list tasks

tasks = []                    

# add task function: priority, task, due date)

def add_task(task, priority, due_date):
    tasks.append({"task": task, "priority": priority, "due_date": due_date})
    print("\nTask added successfully!")

# remove task function

def remove_task(task):
    for t in tasks:
        if t["task"] == task:
            tasks.remove(t)
            print("\nTask removed successfully!")
            return
    print("\nTask not found!")

# view task saved before    

def view_tasks():
    if tasks:
        print("Tasks:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. Task: {t['task']}, Priority: {t['priority']}, Due Date: {t['due_date']}")
    else:
        print("\nNo tasks found!")

# save tasks to file        

def save_tasks_to_file(filename):
    with open(filename, "w") as file:
        json.dump(tasks, file)
    print("\nTasks saved to file successfully!")

def load_tasks_from_file(filename):
    global tasks
    try:
        with open(filename, "r") as file:
            tasks = json.load(file)
        print("\nTasks loaded from file successfully!")
    except FileNotFoundError:
        print("\nNo saved tasks found!")

# initiate code 
# menu options

def main():
    load_tasks_from_file("tasks.json")

    while True:
        print("\n---｡⋆ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆To-Do List ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡  ---\n")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Save Tasks to File")
        print("5. Exit")
        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            task = input("\nEnter task: ")
            priority = input("\nEnter priority (High, Medium, Low): ")
            due_date = input("\nEnter due date: ")
            add_task(task, priority, due_date)
        elif choice == "2":
            task = input("\nEnter task to remove: ")
            remove_task(task)
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            save_tasks_to_file("tasks.json")
        elif choice == "5":
            break
        else:
            print("\nInvalid choice. Please try again.\n")

    save_tasks_to_file("tasks.json")

if __name__ == "__main__":
    main()

