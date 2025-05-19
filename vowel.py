'''
Write a function that takes a sentence as input and returns the number of vowels (a, e, i, o, u) in it. 
Remember to handle both uppercase and lowercase vowels.
'''

user_input = input("Enter a sentence: ")
user_input = user_input.lower()  # convert to lowercase
vowels = "aeiou"

for i in user_input:
  if i in vowels:
    print(f"{i} is a vowel")