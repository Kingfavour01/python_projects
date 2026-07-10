questions = ("How many days are in a week: ",
             "hour many hours are in a day: ",
             "how many days are in the month of June: ",
             "who is the GOAT of football: ",)
options = (("a. 7 ","b. 6 ","c. 5 ","d. 4 ")
          ,("a. 23 ","b. 45 ","c. 24 ","d. 22 ")
          ,("a. 31 ","b. 30 ","c. 28 ","d. 29 ")
          ,("a.Messi ","b. ZLATAN ","c. Ronaldo ","d. FIFA "),)

answers = ("a","c","a","c")
guesses = []
score = 0
question_number = 0


for question in questions:
    print("------------------------------------------------------")
    print(question)
    for option in options[question_number]:
        print(option)

    guess = input("a , b , c , d: ").lower()
    guesses.append(guess)

    if guess == answers[question_number]:
        score += 1
        print("correct")
    else:
        print("incorrect")
        print(f"the correct answer {answers[question_number]}")
    question_number += 1

print("------------------------------------------------------")
print("-------------          RESULT        -----------------")
print("------------------------------------------------------")


print("answers: ", end="")
for answer in answers:
        print(answer,end=" ")
print()



print("guesses: ", end="")
for guess in guesses:
        print(guess,end=" ")
print()

score = int(score / len(questions) * 100)

print(f"your score is {score}% ")













