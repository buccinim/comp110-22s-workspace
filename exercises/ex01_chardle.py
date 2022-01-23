"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730316006"


five_character_word: str = input("Enter a 5-character word: ")
if len(five_character_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()
if type(single_character) != str:
    print("Error: Character must be a single character.")

count: int = 0

print("Searching for " + single_character +  " in " + five_character_word)

if single_character == str((five_character_word[0])): 
    print(single_character + " found at index 0")
    count = count + 1

if single_character == str((five_character_word[1])):
    print(single_character + " found at index 1")
    count = count + 1

if single_character == str((five_character_word[2])):
    print(single_character + " found at index 2")
    count = count + 1

if single_character == str((five_character_word[3])):
    print(single_character + " found at index 3")
    count = count + 1

if single_character == str((five_character_word[4])):
    print(single_character + " found at index 4")
    count = count + 1 



if count == 0:
    print("No instances of " + single_character + " found in " + five_character_word )
else:
    if count == 1:
        print("1 instance of " + single_character + " found in " + five_character_word)
    else:
        if count == 2:
            print("2 instances of " + single_character + " found in " + five_character_word)
        else:
            if count == 3:
                print("3 instances of " + single_character + " found in " + five_character_word)
            else: 
                if count == 4:
                    print("4 instances of " + single_character + " found in " + five_character_word)

    
        
        


