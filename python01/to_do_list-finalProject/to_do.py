import functions
# menu options
# main code

def main():
    functions.load_tasks_from_file("tasks.json")

    while True:
        print ("˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ \n")
        print ("˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ \n")
        print("\n---｡⋆ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆(˶ᵔ ᵕ ᵔ˶)--To-Do List--(˶ᵔ ᵕ ᵔ˶) ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡  ---\n")
        print (" ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆  ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ. ˚ ✩✭ ⋆☆")
        print ("˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ . ˚ ✩✭ ⋆☆ﾟ ⋆ \n")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Save Tasks to File")
        print("5. Exit")
        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            task = input ("\nEnter task: ")
            priority = input("\nEnter priority (High, Medium, Low): ")
            due_date = input("\nEnter due date: ")
            functions.add_task(task, priority, due_date)
        elif choice == "2":
            task = input("\nEnter task to remove: ")
            functions.remove_task(task)
        elif choice == "3":
            functions.view_tasks()
        elif choice == "4":
            functions.save_tasks_to_file("tasks.json")
        elif choice == "5":
            break
        else:
            print("\n(╯°□°)╯︵ ɹoɹɹƎ------Invalid choice. Please try again.--------(╯°□°)╯︵ ɹoɹɹƎ\n")

    functions.save_tasks_to_file("tasks.json")

if __name__ == "__main__":
    main()

