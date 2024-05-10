from models.__init__ import CONN, CURSOR
from sqlite3 import IntegrityError


class User:
    def __init__(self, name):
        self.name = name
        self.id = None

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}')"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        elif len(new_name) < 3:
            raise ValueError("Name must be 3 or more characters")
        else:
            self._name = new_name

    @classmethod
    def find_by_name(cls, name):
        try:
            with CONN:
                CURSOR.execute(
                    """
                       SELECT * FROM users
                        WHERE name = ?;
                    """,
                    (name,),
                )
                row = CURSOR.fetchone()
                return cls.instance_from_db(row) if row else None
        except Exception as e:
            print("Error fetching user by name:", e)

    @classmethod
    def create(cls, name):
        try:
            with CONN:
                CURSOR.execute(
                    """
                        INSERT INTO users (name)
                        VALUES (?);
                    """,
                    (name,),
                )
                CONN.commit()
                user_id = CURSOR.lastrowid
                new_user = cls(name)
                new_user.id = user_id
                return new_user
        except IntegrityError as e:
            print("Name must be provided")
        except Exception as e:
            print("Error creating new user:", e)

    @classmethod
    def instance_from_db(cls, row):
        if row:
            user_id, name = row[0], row[1]
            user = cls(name)
            user.id = user_id
            return user
        return None

    def save(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                        INSERT INTO users (name)
                        VALUES (?);
                    """,
                    (self.name,),
                )
                CONN.commit()
                self.id = CURSOR.lastrowid
        except IntegrityError as e:
            print("Name must be provided")
        except Exception as e:
            print("Error saving user:", e)

    def delete(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                        DELETE FROM users WHERE id = ?;
                    """,
                    (self.id,),
                )
                CONN.commit()
                print(f"{self.name} has been successfully deleted.")
        except Exception as e:
            print("Error deleting user:", e)

    @classmethod
    def create_table(cls):
        try:
            with CONN:
                CURSOR.execute(
                    """
                        CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY,
                            name TEXT
                        );
                    """
                )
        except Exception as e:
            print("Error creating users table:", e)

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
