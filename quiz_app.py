# -----------------------------
# Quiz App - English, Aptitude, Python
# Author: Ramya Markanda
# -----------------------------

# English Questions
english_questions = [
    {
        "question": "Choose the correct spelling:",
        "options": ["A. Recieve", "B. Receive", "C. Recive", "D. Receeve"],
        "answer": "B"
    },
    {
        "question": "Choose the correct synonym of 'Happy':",
        "options": ["A. Sad", "B. Angry", "C. Joyful", "D. Cry"],
        "answer": "C"
    },
    {
        "question": "Choose the correct sentence:",
        "options": [
            "A. She don't like coffee",
            "B. She doesn't likes coffee",
            "C. She doesn't like coffee",
            "D. She don't likes coffee"
        ],
        "answer": "C"
    },
    {
        "question": "Fill in the blank: He ___ to school every day.",
        "options": ["A. go", "B. goes", "C. gone", "D. going"],
        "answer": "B"
    }
]

# Aptitude Questions
aptitude_questions = [
    {
        "question": "What is 25% of 200?",
        "options": ["A. 25", "B. 50", "C. 75", "D. 100"],
        "answer": "B"
    },
    {
        "question": "If 5 pens cost ₹50, what is the cost of 1 pen?",
        "options": ["A. ₹5", "B. ₹8", "C. ₹10", "D. ₹15"],
        "answer": "C"
    },
    {
        "question": "What comes next in the series: 2, 4, 6, 8, ?",
        "options": ["A. 9", "B. 10", "C. 11", "D. 12"],
        "answer": "B"
    },
    {
        "question": "Simplify: 10 + 2 × 5",
        "options": ["A. 60", "B. 20", "C. 30", "D. 50"],
        "answer": "B"
    }
]

# Python Questions
python_questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. function", "C. def", "D. define"],
        "answer": "C"
    },
    {
        "question": "What is the output of: print(2 + 3 * 2)?",
        "options": ["A. 10", "B. 7", "C. 12", "D. 9"],
        "answer": "B"
    },
    {
        "question": "Which data type is used to store True or False?",
        "options": ["A. int", "B. str", "C. bool", "D. float"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. /* */"],
        "answer": "C"
    }
]

# Combine all questions
questions = english_questions + aptitude_questions + python_questions

score = 0

print("===================================")
print("      WELCOME TO QUIZ APP 🎯       ")
print(" Subjects: English | Aptitude | Python")
print("===================================")

# Quiz Loop
for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct ✅")
        score += 1
    else:
        print("Wrong ❌")

# Final Result
print("\n===================================")
print("Quiz Completed 🎉")
print(f"Your Score: {score} / {len(questions)}")

percentage = (score / len(questions)) * 100
print(f"Percentage: {percentage:.2f}%")

if percentage >= 50:
    print("Result: PASS ✅")
else:
    print("Result: FAIL ❌")

print("===================================")
