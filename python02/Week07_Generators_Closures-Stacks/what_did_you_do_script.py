def daily_activities():
    activities = []
    while True:
        new_activity = yield activities
        if new_activity:
            activities.append(new_activity)
            print(", ".join(activities))

activity_gen = daily_activities()
next(activity_gen)  # Initialize the generator

while True:
    try:
        user_input = input("What did you do today or 'exit' to finish? ")
        
        if user_input.lower() == "exit":
            break
        
        if any(char.isdigit() for char in user_input):
            print("Please avoid using numbers in your activity.")
            continue
        
        activities_list = activity_gen.send(user_input.capitalize())
    except KeyboardInterrupt:
        print("\nExiting...")
        break
    except Exception as e:
        print(f"An error occurred: {e}")