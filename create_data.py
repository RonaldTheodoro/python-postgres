import random
import rstr
from faker import Factory
from collections import namedtuple


Employee = namedtuple(
    'employee',
    ['id', 'register_number', 'name', 'phone', 'address', 'salary', 'age']
)


def create_register():
    register_number = create_register_number()
    name = create_name()
    phone = create_phone()
    address = create_address()
    salary = create_salary()
    age = create_age()

    return Employee(register_number, name, phone, address, salary, age)


def create_register_number():
    register_id = create_random_number(13)
    return f'{register_id}'

def create_name():
    fake = Factory.create()
    return fake.name()


def create_phone():
    ddd = create_random_number(2)
    phone = create_random_number(8)
    return f'{ddd}{phone}'


def create_random_number(size):
    return rstr.rstr('0123456789', size)


def create_address():
    fake = Factory.create()
    return fake.address()


def create_salary():
    return float(format(random.uniform(973.0, 5000.0), '.2f'))


def create_age():
    return random.randint(15, 80)
