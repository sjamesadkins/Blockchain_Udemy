names = ['Sam', 'Donovan', 'Harriet', 'Joanna', 'Michael', 'Dave', 'Nathaniel']

for name in names:
    if len(name) > 5 and ('n' or 'N') in name:
        print(len(name))
        print(name)
    
while len(names) > 0:
    names.pop()
    print(names)



