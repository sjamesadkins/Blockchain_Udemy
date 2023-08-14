#formatting
number = 100000000000000
print(f"{number:,}")

#type
blockchain = [1, 2]
print(type(blockchain))

#method/function and append
def add_value():
    blockchain.append([blockchain[-1], 5.3])
    print(blockchain)

add_value()

#text over multiple lines
print("""
Hello World
This is me saying hi on many levels
Bonjour, le Monde
""")
      
#boolean
waiting_for_input = True

#data structures
list = ['milk', 'honey', 'milk']
set = {'milk', 'honey'}
tuple = ('milk', 'honey')
dictionary = {'name':'milk', 'sweetener':'honey'}

#dict comprehension
stats = [('age', 29), ('weight', 72), ('height', 178)]
dict_stats = {key: value for (key, value) in stats}

print(dict_stats)
print(list[1])
print(set)
print(tuple[0])

#range selector for copying a list (because otherwise lists are copied by reference)
my_list = [1,2,3,4]
second_list = [1, 2, 3, 4]
new_list = my_list
new_list[0] = 5
copied_list = second_list[:] #<-- use the [:] syntax to copy the contents rather than reference

print(my_list)
print(new_list)
print(copied_list)


