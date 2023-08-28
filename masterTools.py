import functools

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
lists = ['milk', 'honey', 'milk']
set = {'milk', 'honey'}
tuple = ('milk', 'honey')
dictionary = {'name':'milk', 'sweetener':'honey'}

#dict comprehension
stats = [('age', 29), ('weight', 72), ('height', 178)]
dict_stats = {key: value for (key, value) in stats}

print(dict_stats)
print(lists[1])
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

#map function
simple_list = [1, 2, 3, 4]
def multiply(el):
    return el * 2

print(map(multiply, simple_list))
print(list(map(multiply, simple_list)))

#lambda function
print(list(map(lambda el: el * 2, simple_list)))

#reduce function
age = [40, 50, 60, 70, 80]
print(functools.reduce(lambda x, y: x + y, age))

# * <-- star syntax can be used to turn arguments into a tuple of arguments
def unlimited_arguments(*args):
    print(args)
    for argument in args:
        print(argument)

unlimited_arguments(1, 2, 3, 4)

# star syntax to unpack list
a = [1, 2, 3]
print('Some text: {} {} {}'.format(*a))

#return dictionaries with two stars
def unlimited_arguments(**keyword_args):
    print(keyword_args)
    for k, argument in keyword_args.items():
        print(k, '=', argument)

unlimited_arguments(name='Sam', age=44)

#format()
#difference between strings and lists
#map()
#reduce()
#using * and ** to unpack lists and dictionaries to single values


