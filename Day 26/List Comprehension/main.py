numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

name = "Kerem"
letters_list = [letter for letter in name]
print(letters_list)

range_list = [2 * n for n in range(1,5)]
print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) >= 5]
print(f"{short_names}\n{long_names}")