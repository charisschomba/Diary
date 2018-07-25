import psycopg2
from create_database import createdb_con
from werkzeug.security import generate_password_hash,check_password_hash

conn = createdb_con()
cur = conn.cursor()

class UserSingUp():
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def save(self):
        cur.execute("insert into users (username,email,password) values(%s,%s,%s)",(self.username,self.email,self.password))
        conn.commit()
        conn.close()

    @classmethod
    def get_user_by_email(cls,email):
        cur.execute("select * from users where email = %s",(email,))
        fetch_data = cur.fetchone()
        user_data = cls(fetch_data[1],fetch_data[2],fetch_data[3])
        return user_data

