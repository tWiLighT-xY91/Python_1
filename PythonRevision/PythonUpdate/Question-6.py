# To merge two dictionaries

def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}


print("Enter the name and age:\n ")
name = input("Enter the name: ")
age = input("Enter the age: ")
address = input("Enter the address of the person: ")
dictionary1 = {'names': name, 'age': age}
dictionary2 = {'address': address}

print(merge_dictionaries(dictionary1, dictionary2))
