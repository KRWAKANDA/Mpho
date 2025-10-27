import json
import os

PROGRESS_FILE = "progress.json"

if os.path.exists(PROGRESS_FILE):
    with open(PROGRESS_FILE, "r") as file:
        progress = json.load(file)
else:
    progress = {}


def save_progress():
    with open(PROGRESS_FILE, "w") as file:
        json.dump(progress, file, indent=4)

def get_workout_plan(goal):
    plans = {
        "strength": ["Push-ups: 3x20", "Squats: 3x20", "Deadlifts: 3x30", "Pull-ups: 3x20"],
        "weight loss": ["Jumping jacks: 3x30s", "Burpees: 3x20", "Running: 20 min", "Plank: 3x30s"],
        "endurance": ["Jogging: 30 min", "Cycling: 30 min", "Jump rope: 3x2min", "Mountain climbers: 3x20"],
        "flexibility": ["Yoga: 20 min", "Hamstring stretch: 3x30s", "Cat-Cow stretch: 3x15", "Shoulder stretch: 3x30s"]
    }
    return plans.get(goal.lower(), ["Sorry, I don't have a plan for that goal."])

def get_nutrition_advice(goal):
    advice = {
        "strength": "Focus on high-protein meals: chicken, eggs, tofu, beans. Include complex carbs.",
        "weight loss": "Eat balanced meals, reduce sugar and processed foods, eat more vegetables.",
        "endurance": "Consume carbs for energy: oatmeal, rice, fruits. Stay hydrated.",
        "flexibility": "Maintain balanced nutrition with protein and healthy fats for recovery."
    }
    return advice.get(goal.lower(), "Sorry, I don't have nutrition advice for that goal.")

def log_progress(user, metric, value):
    if user not in progress:
        progress[user] = {}
    progress[user][metric] = value
    save_progress()
    return f"Progress updated: {metric} = {value}"

def chatbot():
    print("👋 Hi! I'm FitBot, your fitness assistant.")
    user = input("What's your name? ")

    while True:
        print("\nOptions: workout | nutrition | log | view progress | exit")
        choice = input("What would you like to do? ").lower()

        if choice == "workout":
            goal = input("What's your fitness goal? (strength, weight loss, endurance, flexibility): ").lower()
            plan = get_workout_plan(goal)
            print("\nHere’s your workout plan:")
            for exercise in plan:
                print(f"- {exercise}")

        elif choice == "nutrition":
            goal = input("What's your fitness goal? (strength, weight loss, endurance, flexibility): ").lower()
            advice = get_nutrition_advice(goal)
            print(f"\nNutrition advice for {goal}: {advice}")

        elif choice == "log":
            metric = input("Which metric do you want to log? (weight, reps, distance, etc.): ").lower()
            value = input(f"Enter your {metric} value: ")
            print(log_progress(user, metric, value))

        elif choice == "view progress":
            user_progress = progress.get(user, {})
            if not user_progress:
                print("No progress logged yet.")
            else:
                print("\nYour progress so far:")
                for metric, value in user_progress.items():
                    print(f"- {metric}: {value}")

        elif choice == "exit":
            print("Goodbye! Keep up the great work 💪")
            break

        else:
            print("I didn't understand that. Please choose a valid option.")

if __name__ == "__main__":
    chatbot()
