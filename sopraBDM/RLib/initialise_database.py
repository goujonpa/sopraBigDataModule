"""Database initialising script

Initialises in a custom way the database

"""
import requests
import json
import random

GENDERS = ['M', 'W', 'N']
MARRIED = [True, False]


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

"""
# Widgets init
for i in range(0, 100):
    data = json.dumps(get_fake_widget(i))
    headers = {
        "Content-Type": "application/json"
    }

    r = requests.post(
        "http://127.0.0.1:8000/api/widgets/?format=json",
        headers=headers,
        data=data
    )

# employees
for i in range(0, 10000):
    data = json.dumps(get_fake_user(i))
    headers = {
        "Content-Type": "application/json"
    }

    r = requests.post(
        "http://127.0.0.1:8000/api/employees/?format=json",
        headers=headers,
        data=data
    )
"""

# notations
d = {
    'employee': 'http://127.0.0.1:8000/api/employees/1/?format=json',
    'widget': 'http://127.0.0.1:8000/api/widgets/2/?format=json',
    'rating': 4
}

data = json.dumps(d)
headers = {
    "Content-Type": "application/json"
}

r = requests.post(
    "http://127.0.0.1:8000/api/notations/?format=json",
    headers=headers,
    data=data
)


print(r.content)
