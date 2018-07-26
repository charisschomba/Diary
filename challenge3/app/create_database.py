import os, psycopg2

def createdb_con(config=None):
    #creating database connection with the right database based on configs
    if config=='testing':
        db_name = os.getenv('testdb')
    else:
        database_name = os.getenv('DB_NAME')

    host = os.getenv('DB_HOST')
    database_name = os.getenv('DB_NAME')
    user = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')

    return psycopg2.connect(
            database = database_name,
            user = user,
            password =password,
            host = host
     )
#This method creates  entries table
def create_entries_table(cursor):
    query = """ CREATE TABLE entries (
            id SERIAL ,
            user_id INTEGER NOT NULL,
            date VARCHAR(20),
            title VARCHAR(255) NOT NULL,
            content VARCHAR(255) NOT NULL,
            PRIMARY KEY (user_id,id),
            FOREIGN KEY (user_id)
            REFERENCES users (id)

            )
             """
    cursor.execute(query)
#creates users table in the database
def create_users_table(cursor):
    query = """
        CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE,
        password VARCHAR(225) NOT NULL
        )
        """
    cursor.execute(query)
def main(config=None):
    conn = createdb_con(config=config)
    with conn.cursor() as cursor:
        cursor.execute("""DROP TABLE IF EXISTS users CASCADE""" )
        cursor.execute("""DROP TABLE IF EXISTS entries CASCADE""" )

        create_users_table(cursor)
        create_entries_table(cursor)

        conn.commit()




    print('Two tables created successfully')

if __name__ == '__main__':
    main()