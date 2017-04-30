import psycopg2


class Database:

    def __init__(self, database_name, user, host='localhost'):
        self.connect(database_name, user, host)
        self.create_cursor()

    def connect(self, database_name, user, host):
        self.connection = psycopg2.connect(
            f"dbname={database_name} user={user} host={host}")

    def create_cursor(self):
        self.cursor = self.connection.cursor(
            cursor_factory=psycopg2.extras.NamedTupleCursor)

    def execute(self, query):
        self.cursor.execute(query)

    def save(self):
        self.connection.commit()

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()
