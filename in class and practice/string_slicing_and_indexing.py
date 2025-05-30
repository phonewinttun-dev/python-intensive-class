
string_variable = "Hello, my name is Phone Wint Tun."
print(string_variable[0]) # string indexing
print(string_variable[-2]) # string reverse indexing
print(string_variable[0:5])  # string slicing  
print(string_variable[0:10:2])  # string slicing with step (start : end : step)

# extracting substring from a string
example_string = "Terracotta pie, banana"
print(example_string[:11])
print(example_string[11:14])
print(example_string[16:])  

#copying a string
copy_string = example_string[::-1]  # reverse the string
print(copy_string)