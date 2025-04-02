questions = [
    "What was the first video game console?",
    "What year did the video game market completely crash?",
    "What video game is commonly accredited for saving the video game industry?",
    "What was the first major 3D video game console?",
    "What were the major video game console brands in the 90s?"
]

easy_questions = [
    "Which country is Nintendo based in?",
    "Which of these companies owns the Xbox brand?",
    "What was the best selling game on the NES?",
    "What is the most recent Nintendo console?"
]

quesion_ans = [
    # Question 1
    "A. Magnavox Odyssey",
    "B. Nintendo Entertainment System",
    "C. Atari 2600",
    "D. Game & Watch",
    # Question 2
    "A. 1989",
    "B. 1993",
    "C. 2010",
    "D. 1983",
    # Question 3
    "A. Sonic the Hedgehog",
    "B. Donkey Kong",
    "C. Super Mario Bros.",
    "D. The Legend of Zelda",
    # Question 4
    "A. Playstation",
    "B. Sega Saturn",
    "C. Nintendo 64",
    "D. Sega Dreamcast",
    # Question 5
    "A. Sega, Nintendo, Playstation",
    "B. Atari, Nintendo, Playstation",
    "C. Xbox, Nintendo, Playstation",
    "D. Sega, Nintendo, Xbox"
]

easy_question_ans = [
    # Question 1
    "A. United States",
    "B. United Kingdom",
    "C. Japan",
    "D. China",
    # Question 2
    "A. Microsoft",
    "B. Nintendo",
    "C. Sony",
    "D. Sega",
    # Question 3
    "A. Super Mario Bros.",
    "B. Duck Hunt",
    "C. Metroid",
    "D. Punch-Out!!",
    # Question 4
    "A. Nintendo Wii",
    "B. Nintendo Wii U",
    "C. Nintendo 3DS",
    "D. Nintendo Switch"
]

def main():
    user_answers = []

    question = 0
    score = 100
    correct = True

    def report_answer(selected_list, selected_question, user_answer="", correct_answer=""):
        user_answers.append(f"{selected_list[selected_question]} \nYour Answer: {user_answer.upper()} \nCorrect Answer: {correct_answer.upper()}")

    print("~-~-~-~-~-Video Game History Quiz~-~-~-~-~-")

    while question < 5:

        if correct:
            print(questions[question])
            for i in range(0,4):
                print(quesion_ans[i + (4 * question)])
        else:
            print(easy_questions[question - 1])
            for i in range(0,4):
                print(easy_question_ans[i + (4 * (question - 1))])

        answer = input("What is your answer? (input letter) \n").lower()

        if answer not in ["a", "b", "c", "d"]:
            print("Oops! Invalid Answer. Please Try Again.")
            continue
        
        if question == 0:
            
            if answer != "a":
                score -= 20
                correct = False
            else:
                correct = True
            report_answer(questions, question, answer, "a")

        elif question == 1:

            if correct:
                if answer != "d":
                    score -= 20
                    correct = False
                else:
                    correct = True
                report_answer(questions, question, answer, "d")
            else:
                if answer != "c":
                    score -= 20
                    correct = False
                else:
                    correct = True
                report_answer(questions, question, answer, "c")

        elif question == 2:

            if correct:
                if answer != "c":
                    score -= 20
                    correct = False
                else:
                    correct = True
                report_answer(questions, question, answer, "c")

            else:

                if answer != "a":
                    score -= 20
                    correct = False
                else:
                    correct = True
                report_answer(questions, question, answer, "a")

        elif question == 3:

            if answer != "a":
                score -= 20
                correct = False
            else:
                correct = True
            report_answer(questions, question, answer, "a")

        elif question == 4:

            if correct:
                if answer != "a":
                    score -= 20
                    correct = False
                else:
                    correct = True
                report_answer(questions, question, answer, "a")
            else:
                if answer != "d":
                    score -= 20
                    correct = False
                else:
                    correct = True
                report_answer(questions, question, answer, "d")

        question += 1

    for entry in user_answers:
        print(entry)

    print(f"SCORE: {score}%")