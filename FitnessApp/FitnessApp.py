"""
    This is an exercise from Group 2 for the topic "Object-oriented Programming" (OOP).  This is a command-line based app using OOP which allows users to:

- Add fitness activities
- View all logged activities
- Calculate total time spent exercising
- Interact through a clean, menu-driven interface
"""


class FitnessTracker:
    # Initialize with empty activity list
    def __init__(self):
        self.activities = []
    # Add a new activity
    def add_activity(self,activity,duration):
        self.activities.append((activity,duration))

        print(f"Added: {activity} for {duration} minutes.")

    #Show all activities
    def view_activities(self):
        if not self.activities:
            print(f"No activities yet.")
        else:
            for i, (act,dur) in enumerate(self.activities,1):
                print(f"{i}. {act} - {dur} mins.")

    #Show total exercise time
    def total_time(self):
        total = sum(d for act,d in self.activities)
        print(f"Total time spent exercising: {total} minutes.")
# User interaction menu
def menu():
    tracker = FitnessTracker()
    while True:
        print("\nFitness Tracker Menu:")

        print("1. Add Activity")

        print("2. View ")

        print("3. Show Total Time")

        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            act = input("Enter activity name: ")
            try:
                dur = int(input("Enter duration (in minutes): "))
                tracker.add_activity(act,dur)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "2":
            tracker.view_activities()

        elif choice == "3":
            tracker.total_time()

        elif choice == "4":
            print("Goodbye! Have a good day!")
            break

        else:
            print("Invalid option.")
# Run the app
menu()

