from models.__init__ import CURSOR, CONN

class Player:
    all = {}

    def __init__(self, name, team, position, points, assists, rebounds, id=None):
        self.id = id
        self.name = name
        self.team = team
        self.position = position
        self.points = points
        self.assists = assists
        self.rebounds = rebounds

    def __repr__(self):
        return f"<Player {self.id}: {self.name}, Team: {self.team}, Position: {self.position}, Points: {self.points}, Assists: {self.assists}, Rebounds: {self.rebounds}>"

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
                            position TEXT,
                            points INTEGER,
                            assists INTEGER,
                            rebounds INTEGER,
                            FOREIGN KEY (team_id) REFERENCES teams(id)
                        );
                    """
                )
        except Exception as e:
            print("Error creating players table:", e)

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
                    (self.name, self.team.id, self.position, self.points, self.assists, self.rebounds)
                )
                self.id = CURSOR.lastrowid
                type(self).all[self.id] = self
        except Exception as e:
            print("Error saving player:", e)

    def update(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                        UPDATE players
                        SET name=?, team_id=?, position=?, points=?, assists=?, rebounds=?
                        WHERE id=?
                    """,
                    (self.name, self.team.id, self.position, self.points, self.assists, self.rebounds, self.id)
                )
        except Exception as e:
            print("Error updating player:", e)

    def delete(self):
        try:
            with CONN:
                CURSOR.execute(
                    """
                        DELETE FROM players
                        WHERE id=?
                    """,
                    (self.id,)
                )
                del type(self).all[self.id]
        except Exception as e:
            print("Error deleting player:", e)

    @classmethod
    def instance_from_db(cls, row):
        player = cls(
            row[1], None, row[3], row[4], row[5], row[6], row[0]
        )
        cls.all[row[0]] = player
        return player

    @classmethod
    def get_all(cls):
        try:
            with CONN:
                CURSOR.execute("SELECT * FROM players")
                rows = CURSOR.fetchall()
                return [cls.instance_from_db(row) for row in rows]
        except Exception as e:
            print("Error fetching players:", e)

    @classmethod
    def find_by_id(cls, id):
        try:
            with CONN:
                CURSOR.execute("SELECT * FROM players WHERE id=?", (id,))
                row = CURSOR.fetchone()
                if row:
                    return cls.instance_from_db(row)
        except Exception as e:
            print("Error finding player by id:", e)