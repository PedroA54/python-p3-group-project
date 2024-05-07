import os


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

    @property
    def nba_team(self):
        return self._nba_team

    @nba_team.setter
    def nba_team(self, nba_team):
        if not isinstance(nba_team, str):
            raise TypeError("Position must be a string")
        self._nba_team = nba_team

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if not isinstance(city, str):
            raise TypeError("city must be a string")
        self._city = city

    @property
    def wins(self):
        return self._wins

    @wins.setter
    def wins(self, wins):
        if not isinstance(wins, int):
            raise TypeError("wins must be a number")
        self._wins = wins

    @property
    def losses(self):
        return self._losses

    @losses.setter
    def losses(self, losses):
        if not isinstance(losses, int):
            raise TypeError("losses must be a number")
        self._losses = losses

    @property
    def championships(self):
        return self._championships

    @championships.setter
    def championships(self, championships):
        if not isinstance(championships, int):
            raise TypeError("championships must be a number")
        self._championships = championships

    @property
    def pg(self):
        return self._pg

    @pg.setter
    def pg(self, pg):
        if not isinstance(pg, str):
            raise TypeError("pg must be a string")
        self._pg = pg

    @property
    def sg(self):
        return self._sg

    @sg.setter
    def sg(self, sg):
        if not isinstance(sg, str):
            raise TypeError("sg must be a string")
        self._sg = sg

    @property
    def sf(self):
        return self._sf

    @sf.setter
    def sf(self, sf):
        if not isinstance(sf, str):
            raise TypeError("sf must be a string")
        self._sf = sf

    @property
    def pf(self):
        return self._pf

    @pf.setter
    def pf(self, pf):
        if not isinstance(pf, str):
            raise TypeError("pf must be a string")
        self._pf = pf

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, c):
        if not isinstance(c, str):
            raise TypeError("c must be a string")
        self._c = c
