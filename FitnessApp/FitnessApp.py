class FitnessApp:
    def __int__(self):
        # Initialize user data
        self.data ={"steps": 0, "calories": 0, "workouts": []}

    def add_steps(self):
        steps = int(input("Enter how many steps you have walked: "))
        self.data["steps"] += steps
        print("Steps updated!")
    def add_calories(self):
        calories = int(input("Enter calories burned: "))
        self.data["calories"] += calories
        print("Calories updated!")
    def add_workout(self):
        workouts = int(input("Enter how many workouts: "))
        self.data["workouts"].append(workouts)
        print("Workouts updated!")