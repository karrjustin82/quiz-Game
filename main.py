print("Python Quiz Game")

questions = [
    {
        "question": "What does CPU stand for?",
        "answer": "central processing unit"
    },
    {
        "question": "What language are we learning?",
        "answer": "python"
    },
    {
        "question": "How many bits are in a byte?",
        "answer": "8"
    },
    {
        "question": "What symbol is used for comments in Python?",
        "answer": "#"
    },
    {
        "question": "What keyword is used to create a function in Python?",
        "answer": "def"
    }
]

score = 0

for q in questions:
    user_answer = input(q["question"] + " ").lower()

    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong!")
        print("Answer:", q["answer"])
        print()

print("Quiz Complete!")
print(f"Your score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100

print(f"Percentage: {percentage:.0f}%")

if percentage >= 80:
    print("Excellent!")
elif percentage >= 60:
    print("Good job!")
else:
    print("Keep practicing!")
