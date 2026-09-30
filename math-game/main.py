import random
print("================================")
print("        MATH QUIZ GAME")
print("================================")
name = input("Enter your name: ")
print("Choose difficulty:")
print("1. Easy")
print("2. Medium")
print("3. Hard")
choice = input("Enter your choice: ")
if choice == "1":
    max_number = 20
elif choice == "2":
    max_number = 50
else:
    max_number = 100
score = 0
total_questions = 10
for i in range(1, total_questions + 1):
    num1 = random.randint(1, max_number)
    num2 = random.randint(1, max_number)
    operation = random.choice(["+", "-"])
    if operation == "+":
        correct_answer = num1 + num2
    else:
        if num2 > num1:
            num1, num2 = num2, num1

        correct_answer = num1 - num2
    print("Question ", i, ":", num1, operation, num2)
    try:
        answer = int(input("Your answer: "))
        if answer == correct_answer:
            print("Correct!")
            score = score + 1
        else:
            print("Wrong! Correct answer:", correct_answer)
    except ValueError:
        print("Invalid answer!")
        print("Correct answer:", correct_answer)
accuracy = (score / total_questions) * 100
print("================================")
print("           RESULT")
print("================================")
print("Player:", name)
print("Score:", score, "/", total_questions)
print("Accuracy:", accuracy, "%")
if score >= 8:
    print("Great job!")
elif score >= 5:
    print("Good effort!")
else:
    print("Keep practicing!")
print("================================")