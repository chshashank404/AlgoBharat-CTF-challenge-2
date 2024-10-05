def decipher_to_numbers(strings):
    # Function to map letters to their corresponding one's digit (A=1, B=2, ..., Z=6)
    def letter_to_digit(letter):
        return (ord(letter.upper()) - ord('A') + 1) % 10

    deciphered_strings = []
    for string in strings:
        deciphered_string = ''.join(str(letter_to_digit(char)) for char in string)
        deciphered_strings.append(deciphered_string)
    
    return deciphered_strings

# Given strings
strings_to_decipher = [
    "NJMLQSORQ", 
    "QOLSRJNQM", 
    "QLJNROSMQ", 
    "JLQRNMOSQ", 
    "JNQSQORLM", 
    "NQSJMROQL"
]

deciphered_clue = decipher_to_numbers(strings_to_decipher)
for original, deciphered in zip(strings_to_decipher, deciphered_clue):
    print(f"{original} -> {deciphered}")
