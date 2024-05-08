import os
from models import CONN, CURSOR  # Corrected import statement


class Team:
    def __init__(self, nba_team, city, wins, losses, championships, pg, sg, sf, pf, c):
        self._nba_team = nba_team
        self._city = city
        self._wins = wins
        self._losses = losses
        self._championships = championships
        self._pg = pg
        self._sg = sg
        self._sf = sf
        self._pf = pf
        self._c = c
        self._players = []

    @property
    def players(self):
        return self._players

    def add_player(self, player):
        self._players.append(player)

    def remove_player(self, player_name):
        self._players = [
            player
            for player in self._players
            if player.name.lower() != player_name.lower()
        ]

    @property
    def nba_team(self):
        return self._nba_team

    @nba_team.setter
    def nba_team(self, nba_team):
        if not isinstance(nba_team, str):
            raise TypeError("Position must be a string")
        self._nba_team = nba_team

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
            print("Error creating teams table:", e)  # Corrected error message

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
                        self.nba_team,
                        self._city,
                        self._wins,
                        self._losses,
                        self._championships,
                        self._pg,
                        self._sg,
                        self._sf,
                        self._pf,
                        self._c,
                    ),
                )
                self.id = CURSOR.lastrowid
                type(self).all[self.id] = self
                return self
        except Exception as e:
            print("Error saving team:", e)


Team.create_table()
