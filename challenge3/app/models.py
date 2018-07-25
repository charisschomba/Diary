import jwt,psycopg2
from create_database import createdb_con
from werkzeug.security import generate_password_hash,check_password_hash

conn = createdb_con()
cur = conn.cursor()

class User():
    def save(self,user):
        cur.execute("insert into users (username,email,password) values(%s,%s,%s)",user)
        conn.commit()
        conn.close()

    @classmethod
    def get_user_by_email(cls,email):
        cur.execute("select * from users where email = %s",(email,))
        fetch_data = cur.fetchone()
        return list([fetch_data])

    def get_pwd_by_email(self,email):
        cur.execute("select password from users where email = %s",(email,))
        fetch_data = cur.fetchone()
        return list(fetch_data)

class Entry():
    """
    This class will store diary entries
    and also have methods that will manipulate
    those entries.
    """

    @staticmethod
    def get_by_id(entryId,user_id):
        """
        This method fetches user entry by its id
        """
        query="select entries.id,date,title,content from entries WHERE user_id={} and id={}".format(user_id,entryId)
        cur.execute(query)
        user_entries = cur.fetchall()
        return user_entries
        conn.close()

    def save(self,entry):
        """
        saves an entry to the database
        """
        cur.execute("insert into entries (user_id,date,title,content) values(%s,%s,%s,%s)",entry)
        conn.commit()
        conn.close()


    def delete_entry(self,entryId):
        """
        deletes an entry
        """
        query = "DELETE FROM entries WHERE entries.id={}".format(entryId)
        cur.execute(query)
        conn.commit()

    def update_entry(self,new_entry,entryId):
        """
        updates a user an entry if it exists with new data
        """
        query = "UPDATE entries SET title = '{}',content= '{}'  WHERE entries.id = {}".format(new_entry[0],new_entry[1],entryId)
        cur.execute(query)
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_entries(user_id):
        """
        This method fetches entries of a user
        """
        query="select entries.id,date,title,content from  entries inner join users on  entries.user_id=users.id WHERE users.id={}".format(user_id)
        cur.execute(query)
        user_entries = cur.fetchall()
        return user_entries
        conn.close()


