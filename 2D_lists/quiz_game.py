# Python quiz game

questions = ("How are you?: ",
             "What is my name?: ",
             "How old am I?:")

options = (("A. good", "B. not good", "C. bad"),
           ("A. Mia", "B. Žiga", "C. Bob"),
           ("A. 19", "B. 20", "C. 21"))

answers = ("C", "B", "C")
question_num = 0
guesses = []
score = 0

for question in questions:
    print("------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer.")

    question_num += 1
print()
print("------------------")
print(f"Your score is {score}!")
print("------------------")