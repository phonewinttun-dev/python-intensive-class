
user_input = input("Enter a sentence: ")
user_input = user_input.lower()  
vowels = "aeiou"
vowel_count = 0
word_count = len(user_input.split())  
letter_count = len(user_input.replace(" ", ""))
  
for i in user_input:
  if i in vowels:
    vowel_count += 1

print(f"Letter count: {letter_count}")
print(f"Word count: {word_count}")
print(f"Vowel count: {vowel_count}")