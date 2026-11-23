questions = [
    {
        "question": "What year was the Boeing 747 first flight?",
        "options": ["1967", "1969", "1985", "2011"],
        "answer": "B",
    },
    {
        "question": "What is the most sold commercial airliner?",
        "options": ["Boeing 747", "Airbus A320", "Boeing 737", "Airbus A 380"],
        "answer": "B",
    },
    {
        "question": "What is the maximum takeoff weight for a Cessna 172S?",
        "options": ["3660lbs", "1550lbs", "2550lbs", "5000lbs"],
        "answer": "C",
    },
    {
        "question": "Hom much horsepower does a Cessna 172S have?",
        "options": ["180", "150", "200","220",],
        "answer": "A",
    },
    {
        "question": "What is the Maximum usable Fuel for a Cessna 172S?",
        "options": ["56 GAL", "50 GAL", "60 GAL", "53 GAL"],
        "answer": "D",
    },
    {
        "question": "How many Concordes were built?",
        "options": ["10", "20", "19", "15"],
        "answer": "B",
    },
    {
        "question": "When was the Wright Brothers first fligh?t",
        "options": ["1910", "1909", "1919", "1903"],
        "answer": "D",
    },
    {
        "question": "What year was the Boeing company started?",
        "options": ["1916", "1945", "1920", "1930"],
        "answer": "A",
    },
    {
        "question": "Waht year was Airbus started?",
        "options": ["1970", "1980", "1995", "2000"],
        "answer": "A",
    },
    {
        "question": "What is the takeoff speed of a Cessna 172?",
        "options": ["60", "55", "63", "74"],
        "answer": "B",
    },
]

def ask_question(question, options, answer):
    # i looked up how to do this but I get that its assigning the letters to a position
    print(question)
    print("A.", options[0])
    print("B.", options[1])
    print("C.", options[2])
    print("D.", options[3])

    choice = input("Your answer: ")

    if choice == answer or choice == answer.lower():
        print("Correct")
        return True
    else:
        print("Incorrect")
        return False


# i looked up how to do the setup for this
def calculate_score(total_questions, num_correct):
    if total_questions == 0:
        return 0
    return (num_correct / total_questions) * 100


def main():
    print("Welcome to Aviation Trivia!")
    user_name = input("Enter your name: ")
    if not user_name:
        user_name = "Player"

    print(f"Good luck, {user_name}!")
    num_correct = 0
    # i looked up how to do everything below this point
    for item in questions:
        if ask_question(item["question"], item["options"], item["answer"]):
            num_correct += 1

    score = calculate_score(len(questions), num_correct)
    print(f"{user_name}, you got {num_correct} out of {len(questions)} correct.")
    print(f"Your score: {score}%")


if __name__ == "__main__":
    main()
