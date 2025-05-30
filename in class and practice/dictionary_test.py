person_info = {'Name' : 'George',
               'Age' : 20}

for key,value in person_info.items():
    print(f"{key} : {value}")

print(person_info.keys())

print(person_info.values())

print(person_info['Age']) #accessing the data from dictionary using key 

data = person_info.popitem()

print(f'Removed item: {data}')

#unpacking