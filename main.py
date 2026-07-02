from art import art
from morse import MorseCode

print(art)

morse_code = MorseCode()

while True:
    operation = input("Do you wish to Encode or Decode? (e for EXIT)\n").lower()

    if operation == "e":
        break
    elif operation == 'encode':
        text = input("Enter your text here: \n")
        code = morse_code.encode(text)
        print("Your Morse Code is: {}".format(code), end='\n')
    elif operation == 'decode':
        text = morse_code.decode()
        print(text, end='\n')
    else:
        print("OOPS! You have an typo error, make sure to write it right.")
    



