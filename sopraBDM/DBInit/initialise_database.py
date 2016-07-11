"""Database initialising script

Initialises in a custom way the database

"""
import requests
import json
import random

GENDERS = ['M', 'W', 'N']
MARRIED = [True, False]
MAX_EMPLOYEES = 6040
MAX_WIDGETS = 100


def random_string_date():
    return (
        str(random.randint(1950, 2016)) + '-' +
        str(random.randint(1, 12)) + '-' +
        str(random.randint(1, 28))
    )


def get_fake_user(user_number):
    return {
        'last_name': 'last_name' + str(user_number),
        'first_name': 'first_name' + str(user_number),
        'birth_date': random_string_date(),
        'joined_date': random_string_date(),
        'salary': random.randint(1000, 20000),
        'phone': '06' + str(user_number).zfill(8),
        'performance_indice': random.randint(0, 5),
        'gender': random.choice(GENDERS),
        'children_number': random.randint(0, 15),
        'adress': 'address' + str(user_number),
        'mail': 'user' + str(user_number) + '@gmail.com',
        'married': random.choice(MARRIED)
    }


def get_fake_widget(widget_number):
    return {
            'name': 'name' + str(widget_number),
            'author': 'author' + str(widget_number),
            'description': 'description' + str(widget_number)
    }

################################################################################
# WIDGETS INIT


for i in range(0, MAX_WIDGETS):
    data = json.dumps(get_fake_widget(i))
    headers = {
        "Content-Type": "application/json"
    }

    r = requests.post(
        "http://127.0.0.1:8000/api/widgets/?format=json",
        headers=headers,
        data=data
    )


################################################################################
# EMPLOYEES INIT


for i in range(0, 6040):
    data = json.dumps(get_fake_user(i))
    headers = {
        "Content-Type": "application/json"
    }

    r = requests.post(
        "http://127.0.0.1:8000/api/employees/?format=json",
        headers=headers,
        data=data
    )


################################################################################
# NOTATIONS
# We use the movielens dataset to fake our test dataset


with open("./ratings.dat") as f:
    for line in f:
        l = line.split(':')
        employee_id = int(l[0])
        if employee_id <= MAX_EMPLOYEES:
            widget_id = int(l[2])
            if widget_id <= MAX_WIDGETS:
                rating = int(l[4])
                d = {
                    'employee': 'http://127.0.0.1:8000/api/employees/' + str(employee_id) + '/?format=json',
                    'widget': 'http://127.0.0.1:8000/api/widgets/' + str(widget_id) + '/?format=json',
                    'rating': rating
                }
                print("\n\nADDED =====")
                print(d)
                data = json.dumps(d)
                headers = {
                    "Content-Type": "application/json"
                }

                r = requests.post(
                    "http://127.0.0.1:8000/api/notations/?format=json",
                    headers=headers,
                    data=data
                )
        else:
            break
print('bsr')
