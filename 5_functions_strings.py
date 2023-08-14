import functools

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

