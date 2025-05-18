id_number = str(input("Enter your ID number: "))
id_checker = id_number.lower().startswith("ykpt")
print(id_number)
id_number = id_number.upper()  # Convert the ID number to uppercase
print(id_checker)  # Check if the ID number starts with "YKPT" and print the result
print(id_number)  # Print the ID number in uppercase
# print(id_number.isalnum)  #white space and special characters are not alphanumeric
id_number_space = id_number.replace(" ", "")  # Remove spaces from the ID number
# print(id_number.replace(" ", ""))  # Remove spaces from the ID number
print(id_number_space.isalnum())  # Check if the ID number is alphanumeric