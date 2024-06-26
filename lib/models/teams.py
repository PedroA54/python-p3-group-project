from models import CONN, CURSOR  # Corrected import statement
from sqlite3 import IntegrityError
import os


class Team:
    all = {}

    def __init__(
        self,
        id,
        team,
        city,
        wins,
        losses,
        championships,
        pg,
        sg,
        sf,
        pf,
        c,
    ):
        self.id = id
        self.team = team
        self.city = city
        self.wins = wins
        self.losses = losses
        self.championships = championships

        self.pg = pg
        self.sg = sg
        self.sf = sf
        self.pf = pf
        self.c = c
        self._players = []

    def __repr__(self):
        return f"<Team {self.id}: {self.team}, {self.city}, Wins: {self.wins}, Losses: {self.losses}, Championships: {self.championships}>"

    def players(self):
        sql = """
            SELECT * FROM players WHERE team_id = ?
        """

        player_rows = CURSOR.execute(sql, (self.id,)).fetchall()
        from players import Players

        return [Players.instance_from_db(player_row) for player_row in player_rows]

    @classmethod
    def create_table(cls):
        try:
            with CONN:
                CURSOR.execute(
                    """
                        CREATE TABLE IF NOT EXISTS teams (
                            id INTEGER PRIMARY KEY,
                            nba_team TEXT NOT NULL,
                            city TEXT NOT NULL,
                            wins INTEGER,
                            losses INTEGER,
                            championships INTEGER,
                            pg TEXT,
                            sg TEXT,
                            sf TEXT,
                            pf TEXT,
                            c TEXT
                        );
                    """
                )
        except Exception as e:
            print("Error creating teams table:", e)

    @classmethod
    def drop_table(cls):
        try:
            with CONN:
                CURSOR.execute(
                    """
                        DROP TABLE IF EXISTS teams;
                    """
                )
        except Exception as e:
            print("Error dropping teams table:", e)

    def save(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                        INSERT INTO teams (nba_team, city, wins, losses, championships, pg, sg, sf, pf, c)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                    """,
                    (
                        self.team,
                        self.city,
                        self.wins,
                        self.losses,
                        self.championships,
                        self.pg,
                        self.sg,
                        self.sf,
                        self.pf,
                        self.c,
                    ),
                )
                self.id = CURSOR.lastrowid
                type(self).all[self.id] = self
        except Exception as e:
            print("Error saving team:", e)

    def update(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                        UPDATE teams
                        SET team=?, city=?, wins=?, losses=?, championships=?, pg=?, sg=?, sf=?, pf=?, c=?
                        WHERE id=?
                    """,
                    (
                        self.id,
                        self.team,
                        self.city,
                        self.wins,
                        self.losses,
                        self.championships,
                        self.pg,
                        self.sg,
                        self.sf,
                        self.pf,
                        self.c,
                    ),
                )
        except Exception as e:
            print("Error updating team:", e)

    def delete(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                        DELETE FROM teams
                        WHERE id=?
                    """,
                    (self.id,),
                )
                del type(self).all[self.id]
        except Exception as e:
            print("Error deleting team:", e)

    @classmethod
    def instance_from_db(cls, row):
        team = cls(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
            row[7],
            row[8],
            row[9],
            row[10],
        )
        cls.all[row[0]] = team
        return team

    @classmethod
    def get_all(cls):
        try:
            with CONN:
                CURSOR.execute("SELECT * FROM teams")
                rows = CURSOR.fetchall()
                return [cls.instance_from_db(row) for row in rows]
        except Exception as e:
            print("Error fetching teams:", e)

    @classmethod
    def find_by_id(cls, id):
        try:
            with CONN:
                CURSOR.execute("SELECT * FROM teams WHERE id=?", (id,))
                row = CURSOR.fetchone()
                if row:
                    return cls.instance_from_db(row)
        except Exception as e:
            print("Error finding team by id:", e)

    @classmethod
    def find_by_city(cls, city):
        try:
            with CONN:
                CURSOR.execute(
                    "SELECT * FROM teams WHERE LOWER(city) LIKE LOWER(?)",
                    (f"%{city}%",),
                )
                row = CURSOR.fetchone()
                if row:
                    return cls.instance_from_db(row)
        except Exception as e:
            print("Error finding team by name:", e)

    @classmethod
    def find_by_name(cls, name):
        try:
            with CONN:
                CURSOR.execute(
                    "SELECT * FROM teams WHERE LOWER(team) LIKE LOWER(?)",
                    (f"%{name}%",),
                )
                row = CURSOR.fetchone()
                if row:
                    return cls.instance_from_db(row)
        except Exception as e:
            print("Error finding team by name:", e)

    def add_player(self, player):
        self._players.append(player)

    def remove_player(self, player_name):
        self._players = [
            player
            for player in self._players
            if player.name.lower() != player_name.lower()
        ]
