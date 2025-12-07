with open("my_file.txt", mode="r") as file: #with keyword closes the file after indented lines of codes
    contents = file.read()
    print(contents)

with open("my_file.txt", mode="a") as file:
    file.write("New text.\n")

with open("new_file.txt", mode="w") as file:
    file.write("New text.\n")

