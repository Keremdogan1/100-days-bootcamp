from random import randint

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = {student:randint(0, 100) for student in names}
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}

print(passed_students)