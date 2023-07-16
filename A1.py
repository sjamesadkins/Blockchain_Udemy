#1
name = input("Enter your name: ")

age = input("Enter your age: ")

#2
def name_age(name, age):
    return print('My name is ' + name + ' and I am ' + age + ' years old.')


name_age(name, age)

#3
def print_data_string(a, b):
    return print(a + ' ' + b)

print_data_string('Audi', str(6000))


#4
def number_of_decades_alive(age):
    decades_alive = age // 10
    return decades_alive

print(number_of_decades_alive(44))
print(number_of_decades_alive(8))
print(number_of_decades_alive(99))

