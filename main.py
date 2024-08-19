import random

questions = {
    "Andhra Pradesh": "Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla",
    "Jharkhand": "Ranchi",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Madhya Pradesh": "Bhopal",
    "Maharashtra": "Mumbai",
    "Manipur": "Imphal",
    "Meghalaya": "Shillong",
    "Mizoram": "Aizawl",
    "Nagaland": "Kohima",
    "Odisha": "Bhubaneswar",
    "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur",
    "Sikkim": "Gangtok",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Tripura": "Agartala",
    "Uttar Pradesh": "Lucknow",
    "Uttarakhand": "Dehradun",
    "West Bengal": "Kolkata"
}

def run_quiz(student_name):
    score = 0
    states = list(questions.keys())
    random.shuffle(states)
    
    for i, state in enumerate(states[:5], 1):
        print(f"Q{i}: What is the capital of {state}?")
        answer = input("Your answer: ").strip()
        
        if answer.lower() == questions[state].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {questions[state]}.")
        
        print()
    
    print(f"{student_name}, your final score is {score}/5\n")
    return score

def conduct_quiz():
    scoreboard = {}
    highest_score = 0
    top_student = ""
    
    while True:
        student_name = input("Enter the student's name (or type 'done' to finish): ").strip()
        if student_name.lower() == 'done':
            break
        
        score = run_quiz(student_name)
        scoreboard[student_name] = score
        

        if score > highest_score:
            highest_score = score
            top_student = student_name
    

    print("\nFinal Scoreboard:")
    for name, score in scoreboard.items():
        print(f"{name}: {score}/5")
    
    print(f"\nThe highest score is {highest_score}/5 by {top_student}!")

if __name__ == "__main__":
    print("Welcome to the States and Capitals Quiz Competition!")
    conduct_quiz()
