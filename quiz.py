import random
import requests
import html

def get_questions():
    url = "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=multiple"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['results']
    else:
        print(f"Failed to fetch data, status code: {response.status_code}")
        return []

def present_questions(question, index):
    print(f"Question {index + 1}: {html.unescape(question['question'])}")
    choices = question['incorrect_answers'] + [question['correct_answer']]
    random.shuffle(choices)
    for i, choice in enumerate(choices):
        print(f"{i + 1}. {html.unescape(choice)}")
    # Return the index of the correct answer (1-based index)
    return choices.index(question['correct_answer']) + 1

def main():
    print("Welcome to the Quiz!\n")
    questions = get_questions()
    if not questions:
        print("Questions not available")
        return
    
    score = 0
    total_questions = len(questions)
    
    for i, question in enumerate(questions):
        correct_choice_number = present_questions(question, i)
        user_answer = input("Your answer (enter number): ")
        try:
            user_answer = int(user_answer)
            if user_answer < 1 or user_answer > len(question['incorrect_answers']) + 1:
                print("Invalid input. Please enter a number corresponding to the options.")
                continue
            if user_answer == correct_choice_number:
                print("Correct!\n")
                score += 1
            else:
                print(f"Incorrect. The correct answer was option {correct_choice_number}.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")
            continue
    
    print(f"Quiz Completed!\nYour score is {score}/{total_questions}")

if __name__ == "__main__":
    main()
