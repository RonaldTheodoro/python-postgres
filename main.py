from database import Database
from create_data import create_register


def main():
    database = Database('data', 'postgres', host='192.168.0.100')

    database.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            id SERIAL PRIMARY KEY,
            register_number VARCHAR(13) NOT NULL UNIQUE,
            name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL,
            address VARCHAR(255) NOT NULL,
            salary REAL NOT NULL,
            age INT NOT NULL
        )
    """)

    for conut in range(1000):
        employee = create_register()
        database.execute(create_query(
            conut,
            employee.register_number,
            employee.name,
            employee.phone,
            employee.address,
            employee.salary,
            employee.age
        ))
        database.save()

    database.close()


def create_query(conut, register_number, name, phone, address, salary, age):
    QUERY = """
        INSERT INTO employee (
            register_number, name, phone, address, salary, age
        ) VALUES ('{}', '{}', '{}', '{}', {}, {})
    """
    print(conut, register_number, name, phone, address, salary, age)
    return QUERY.format(register_number, name, phone, address, salary, age)


if __name__ == '__main__':
    main()
