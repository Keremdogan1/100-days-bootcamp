from art import logo

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
new_letters = [""] * 26

def letters_shift(letters, shift):
    shift %= 26
    for i in range(26-shift):
        new_letters[i]=letters[i+shift]
    for i in range(shift):
        new_letters[i-25] = letters[i]

def crypt(code, letters, shift, select):
    letters_shift(letters, shift)

    code_list = [char for char in code]
    code_list_len = len(code_list)

    for index in range(code_list_len):
        if code_list[index] in letters:
            for i in range(26):
                if code_list[index] == letters[i]:
                    code_list[index] = new_letters[i]
                    break

    code_list_string = "".join(code_list)
    if select == 1:
        print(f"Here's the encoded result: {code_list_string}")
    else:
        print(f"Here's the decoded result: {code_list_string}")

run = True

while run:
    print(logo)

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    code = input("Enter the code which you want to encrypt: ")
    code = code.lower()
    shift = int(input("Enter the shift amount: "))

    if direction == "encode":
        crypt(code, letters, shift, 1)
    elif direction == "decode":
        crypt(code, letters, (26-shift), 2)
    else:
        print("Wrong input!")

    wanna_continue = input("Type 'yes' if you want to do again. Otherwise type 'no':\n").lower()

    if wanna_continue == "yes":
        run = True
    else:
        print("Goodbye!")
        run = False