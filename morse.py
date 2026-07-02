
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}

class MorseCode:
    def __init__(self):
        pass

    def encode(self, text):
        list_text = list(text.upper())
        return ' '.join([MORSE_CODE_DICT[letter] for letter in list_text])


    def decode(self):
        print(
            """
            Type morse code using '.', '-', using a spaces between letters
            and '/' between words
            """
        )
        REVERSE_MORSE = {value: key for key, value in MORSE_CODE_DICT.items()}
    
        code = input("\n").split("/")
        words = []
        
        for word in code:
            letters = word.split()
            decoded_word = ''.join(REVERSE_MORSE[letter] for letter in letters)
            words.append(decoded_word)
        
        return ' '.join(words)

