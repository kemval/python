import json

# Store list tasks

tasks = []                    

# create a function that creates dictionary and then it adds it into the task list

def add_task(task, priority, due_date):
    tasks.append({"task": task, "priority": priority, "due_date": due_date})
    print("\nTask added successfully!")

# remove tasks function

def remove_task(task):
    for task in tasks:
        if task["task"] == task:
            tasks.remove(task)
            print("\nTask removed successfully!")
            return
    print("\nTask not found!")


# view tasks saved before function  

def view_tasks():
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. Task: {task['task']}, Priority: {task['priority']}, Due Date: {task['due_date']}")
    else:
        print("\nNo tasks found!")


# save tasks to file        
# "w" (write mode)
# "r" (read mode)

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

