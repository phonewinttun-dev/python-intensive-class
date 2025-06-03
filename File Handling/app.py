'''
file = open("students.txt", "r")

#file reading
data = file.read() 
file.seek(0) #reset the reading 
data2 = file.read()
file.seek(0)
data3 = file.readlines() #will print the data as an item in a list
file.seek(0)
data4 = file.readline()

print(file)
print(data)
print(data2)
print(data3)
print(data4)
file.close()

#.read() -> read the whole file
#.readline() -> read one line only
#.readlines() -> will print the data as an item in a list
'''
'''
#file writing (w -> overwrite)
file = open("students.txt", "w")
data = "Test"
file.write(data)
file.close()
'''
'''
#file appending (will add new data without overwriting)
file = open("students.txt", "a")
data = "Test6"
file.write(data)
file.close()
'''

#close file automatically after the operation is done
'''
'''
with open ("./students.txt", "r") as file:
    content = file.read()
    print(content)