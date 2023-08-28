import random
import datetime

random_number_1 = round(random.random(),2)
print(random_number_1)

random_number_2 = round(random.random() * 10, 2)
print(random_number_2)

# random_datetime = datetime.datetime(2023, 11, 9, 4, 56, 44, 33)
# print(random_datetime)


random_datetime = datetime.datetime.now()
print(random_datetime)

random_number_3 = str(random_datetime) + str(random_number_1) + str(random_number_2)
print(random_number_3)