from models.__init__ import CONN, CURSOR
from models.teams import Team


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Player {self.id}: {self.name}"

    #! Properties

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
    def get_roster(cls):
        CURSOR.execute(
            """
               SELECT * from players
            """
        )
        rows = CURSOR.fetchall()
        return [cls(row[1], row[2], row[0]) for row in rows]

    @property
    def name(self):
        return self._name

    def delete(self):
        CURSOR.execute(
            """
                DELETE FROM users
            WHERE id = ?
            """,
            (self.id,),
        )
        CONN.commit()
        self.id = None
        return self
