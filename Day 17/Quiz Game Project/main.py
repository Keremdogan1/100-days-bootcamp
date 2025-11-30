from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for index in range(len(question_data)):
    question_bank.append(Question(question_data[index]["question"],question_data[index]["correct_answer"]))

quiz = QuizBrain(question_bank)
correct = 0
total = 0

while(quiz.still_has_questions()):
    quiz.next_question()

print("You've completed the quiz!")
print(f"You final score is: {quiz.score}/{len(question_bank)}")

