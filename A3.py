#Create a list of person dictionaries with a name, age, and list of hobbies for each person. 

persons = [{'name':'Sam', 'age': 19, 'hobbies': ('brewing', 'guitar')}, {'name': 'Marissa', 'age': 36, 'hobbies': ('quality control', 'hiking')}, {'name': 'Kevin', 'age': 43, 'hobbies': ('guitar', 'records')}]

#Use a list comprehension to convert this list of persons into a list of names (of the persons)

print([el['name'] for el in persons])

#Use a list comprehension to check whether all persons are older than 20

print([el['age'] > 20 for el in persons])

#Copy the person list such that you can safely edit the name of the first person (without changing the orignal list)

# new_persons = persons[:]

copied_persons = [person.copy() for person in persons]
copied_persons[0]['name'] = 'Max'
print(persons)
print(copied_persons)

#Unpack the persons of the original list into different variables and output these variables

a, b, c = persons
print(a)

print(b)

print(c)

