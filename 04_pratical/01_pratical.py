# A pangram is a sentence that contains all the letters of the English alphabet at
# least once, for example: The quick brown fox jumps over the lazy dog. Your
# task here is to write a function to check a sentence to see if it is a pangram or
# not

def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in alphabet:
        if letter not in sentence.lower():
            return False

    return True

sentence = "The quick brown fox jumps over the lazy dog"

if is_pangram(sentence):
    print("It is a  pangram.")
else:
    print("it is not a pangram.")

              