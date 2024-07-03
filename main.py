import psycopg2
from typing import Optional


conn = psycopg2.connect(database = 'n48',
                        user = 'postgres',
                        host = 'localhost',
                        password = '123',
                        port = '5432')

cursor = conn.cursor()


import psycopg2

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        conn = psycopg2.connect(
            dbname="your_dbname",
            user="your_username",
            password="your_password",
            host="your_host",
            port="your_port"
        )
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id",
            (self.name, self.email)
        )
        self.id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def get_users():
        conn = psycopg2.connect(
            dbname="your_dbname",
            user="your_username",
            password="your_password",
            host="your_host",
            port="your_port"
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        cur.close()
        conn.close()
        return users

    @staticmethod
    def get_user(user_id):
        conn = psycopg2.connect(
            dbname="your_dbname",
            user="your_username",
            password="your_password",
            host="your_host",
            port="your_port"
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cur.fetchone()
        cur.close()
        conn.close()
        return user

    @staticmethod
    def delete_user(user_id):
        conn = psycopg2.connect(
            dbname="your_dbname",
            user="your_username",
            password="your_password",
            host="your_host",
            port="your_port"
        )
        cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        cur.close()
        conn.close()

    def update_user(self, user_id, name, email):
        conn = psycopg2.connect(
            dbname="your_dbname",
            user="your_username",
            password="your_password",
            host="your_host",
            port="your_port"
        )
        cur = conn.cursor()
        cur.execute(
            "UPDATE users SET name = %s, email = %s WHERE id = %s",
            (name, email, user_id)
        )
        conn.commit()
        cur.close()
        conn.close()

new_user = User(name="Ali", email="ali@example.com")
new_user.save()

all_users = User.get_users()
print(all_users)

user = User.get_user(new_user.id)
print(user)

new_user.update_user(new_user.id, "Ali Ahmed", "ali.ahmed@example.com")

User.delete_user(new_user.id)





