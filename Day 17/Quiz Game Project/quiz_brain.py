class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 1
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number <= len(self.question_list)

    def next_question(self,):
        user_answer = input(f"Q.{self.question_number}: {self.question_list[self.question_number - 1].question} (True/False)? : ").lower()
        self.check_answer(user_answer, self.question_list[self.question_number - 1].correct_answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Print you got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")
        print("\n")