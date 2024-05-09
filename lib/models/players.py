import os
from models.__init__ import CONN, CURSOR
from sqlite3 import IntegrityError


class Players:
    all = {}

    def __init__(self, name, team_id, position, points, assists, rebounds, id):
        self.name = name
        self.team_id = team_id
        self.position = position
        self.points = points
        self.assists = assists
        self.rebounds = rebounds
        self.id = id

    def __repr__(self):
        return f"<Player Name: {self.name}, Team: {self.team().name}, Position: {self.position}, Points: {self.points}, Assists: {self.assists}, Rebounds: {self.rebounds}>"

    def team(self):
        from teams import Team

        return Team.find_by_id(self.team_id)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        self._name = name

    @property
    def team_id(self):
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        from teams import Team

        team = Team.find_by_id(team_id)
        if not isinstance(team, Team):
            raise TypeError("Team not found.")
        self._team_id = team_id

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        if not isinstance(position, str):
            raise TypeError("Position must be a string")
        self._position = position

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, points):
        if not isinstance(points, (int, float)):
            raise TypeError("Points must be a number")
        self._points = points

    @property
    def assists(self):
        return self._assists

    @assists.setter
    def assists(self, assists):
        if not isinstance(assists, (int, float)):
            raise TypeError("Assists must be a number")
        self._assists = assists

    @property
    def rebounds(self):
        return self._rebounds

    @rebounds.setter
    def rebounds(self, rebounds):
        if not isinstance(rebounds, (int, float)):
            raise TypeError("Rebounds must be a number")
        self._rebounds = rebounds

    # Class and Association Methods go here

    @classmethod
    def instance_from_db(cls, row):
        player = cls(
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
            row[0],
        )
        cls.all[row[0]] = player
        return player

    @classmethod
    def find_by_id(cls, id):
        try:
            with CONN:
                CURSOR.execute("SELECT * FROM players WHERE id=?", (id,))
                row = CURSOR.fetchone()
                if row:
                    return cls.instance_from_db(row)
        except Exception as e:
            print("Error finding team by id:", e)

    @classmethod
    def find_by_name(cls, name):
        try:
            with CONN:
                CURSOR.execute("SELECT * FROM players WHERE name=?", (name,))
                row = CURSOR.fetchone()
                if row:
                    return cls.instance_from_db(row)
        except Exception as e:
            print("Error finding team by id:", e)

    @classmethod
    def create_table(cls):
        try:
            with CONN:
                CURSOR.execute(
                    """
                        CREATE TABLE IF NOT EXISTS players (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            team_id INTEGER,
                            position TEXT NOT NULL,
                            points REAL,
                            assists REAL,
                            rebound REAL,
                            FOREIGN KEY (team_id) REFERENCE teams(id)
                            
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
                        DROP TABLE IF EXISTS players;
                    """
                )
        except Exception as e:
            print("Error dropping players table:", e)

    def save(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                        INSERT INTO players (name, team_id, position, points, assists, rebounds)
                        VALUES (?, ?, ?, ?, ?, ?);
                    """,
                    (
                        self.name,
                        self.team_id,
                        self.position,
                        self.points,
                        self.assists,
                        self.rebounds,
                    ),
                )
                self.id = CURSOR.lastrowid
                type(self).all[self.id] = self
                return self
        except Exception as e:
            print("Error saving player:", e)
