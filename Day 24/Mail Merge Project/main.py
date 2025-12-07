#TODO: Create a letter using starting_letter.txt
with open("Input/Names/invited_names.txt") as invited_names:
    for line in invited_names:
        line = line.replace("\n", "")
        with open("Input/Letters/starting_letter.txt") as starting_letter:
            contents = starting_letter.read()
            contents = contents.replace("[name]", line)
            with open(f"Output/ReadyToSend/{line}.txt", "a") as file_to_send:
                file_to_send.write(contents)

#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp