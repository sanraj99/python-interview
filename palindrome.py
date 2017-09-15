from string import punctuation
import re

"""take a phrase and convert to all lowercase letters and ignore punctuation marks and whitespaces,
	   if it matches the reverse spelling then it is a palindrome
"""
def string_palindrome(phrase):
    phrase_letters = [c for c in phrase.lower() if c.isalpha()]
    print phrase_letters
    return (phrase_letters == phrase_letters[::-1])

inputPhrase = raw_input("Enter a Sentence : ")
if string_palindrome(inputPhrase):
	print '"%s" is a palindrome' % inputPhrase
else:
    print '"%s" is not a palindrome' % inputPhrase

def number_palindrome(number):
    return int(str(number)[::-1]) == number

inputNumber=76382736487236482736
if number_palindrome(inputNumber):
    print(str(inputNumber) + " is a palindrome")
else:
    print(str(inputNumber) + " not a palindrome")




