import pandas

student_dict = {
    "student": ["Kerem", "James" ,"Lily"],
    "score": [98, 56, 76]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

print()

for (key, value) in student_data_frame.items():
    print(value)

print()

for (index, row) in student_data_frame.iterrows():
    print(row)

print()

for (index, row) in student_data_frame.iterrows():
    if row.student == "Kerem":
        print(row.student)