from models.__init__ import CONN, CURSOR
import click


class User:
    current_user = None

    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def __repr__(self):
        return f"User ID: {self.id} || User Name: {self.name}"

    @classmethod
    def find_by_name(cls, name):
        try:
            return cls.get_user_by_name(name)
        except Exception as e:
            print("An error occurred while finding user by name:", e)
            return None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        elif not 1 <= len(name) <= 20:
            raise ValueError("Name must be between 1 and 20 characters")
        else:
            self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if hasattr(self, "id"):
            raise AttributeError("You are not allowed to change the id")
        else:
            self._id = id

    # CRUD operations

    def save(self):
        sql = """ 
            INSERT INTO users (name, id)
            VALUES(?, ?)
        """
        try:
            CURSOR.execute(sql, (self.name, self.id))
            CONN.commit()
            self._id = CURSOR.lastrowid
        except Exception as e:
            print("An Error Occurred:", e)
            raise Exception

        return self

    def update(self):
        sql = """
            UPDATE users
            SET name = ?
            WHERE id = ?
        """
        try:
            CURSOR.execute(sql, (self.name, self.id))
            CONN.commit()
        except Exception as e:
            print("An Error Occurred:", e)
            raise Exception

    def delete(self):
        sql = """ 
            DELETE FROM users
            WHERE id = ?
        """
        try:
            CURSOR.execute(sql, (self.id,))
            CONN.commit()
        except Exception as e:
            print("An Error Occurred:", e)
            raise Exception

    @classmethod
    def create(cls, name, id=None):
        new_user = cls(name, id)
        new_user.save()
        return new_user

    @classmethod
    def instance_from_db(cls, row):
        return cls(row[1], row[0])

    @classmethod
    def get_all(cls, limit=None, offset=None):
        try:
            query = "SELECT * FROM users"
            if limit is not None and offset is not None:
                query += f" LIMIT {limit} OFFSET {offset}"
            CURSOR.execute(query)
            rows = CURSOR.fetchall()
            return [cls(row[1], row[0]) for row in rows]
        except Exception as e:
            CONN.rollback()
            print("An Error Occurred: ", e)
            raise Exception

    @classmethod
    def get_user_by_id(cls, id):
        try:
            query = "SELECT * FROM users WHERE id = ?"
            CURSOR.execute(query, (id,))
            obj = CURSOR.fetchone()
            return cls(obj[1], obj[0])
        except Exception as e:
            CONN.rollback()
            print("An Error Occurred: ", e)
            raise Exception

    @classmethod
    def get_user_by_name(cls, name):
        try:
            query = "SELECT * FROM users WHERE name = ?"
            CURSOR.execute(query, (name,))
            obj = CURSOR.fetchone()
            return cls(obj[1], obj[0])
        except Exception as e:
            CONN.rollback()
            print("An Error Occurred: ", e)
            raise Exception

    @classmethod
    def set_current_user(cls, user):
        if not cls.current_user:
            cls.current_user = user
        else:
            print("User already logged in")
            click.pause()


@classmethod
def create_table(cls):
    try:
        with CONN:
            CURSOR.execute(
                """
                        CREATE TABLE IF NOT EXISTS user (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            condition TEXT,
                            phase TEXT NOT NULL,
                            is_alive BOOLEAN NOT NULL
                        );
                    """
            )
    except Exception as e:
        return e

    @classmethod
    def drop_table(cls):
        try:
            with CONN:
                CURSOR.execute(
                    """
                    DROP TABLE IF EXISTS users;
                """
                )
        except Exception as e:
            print("Error dropping users table:", e)
