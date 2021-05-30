from utils import team_name_convert

import math

class Team():
    id_list = None
    abbr_dict = None

    def __init__(self):
        if Team.id_list is None or Team.abbr_dict is None:
            Team.init_class()

        self.team_id = None
        self.name = None
        self.group = None
        self.odds = None
        self.log_odds = None

    def __str__(self):
        return "(%02d) %s %s %d %.2f" % (self.team_id, self.name, self.group, self.odds, self.log_odds)

    def __eq__(self, other):
        o = Team.from_ambig(other)
        if o is not None:
            return self.team_id == o.team_id
        return NotImplemented

    def encode(self):
        return {
            'id': self.team_id,
            'name': self.name,
            'group': self.group,
            'odds': self.odds,
            'log_odds': self.log_odds
        }

    @property
    def is_active(self):
        return self.active

    @property
    def is_push(self):
        return self == Team.from_name('PUSH')

    @property
    def is_ou(self):
        return self == Team.from_name('OVER') or self == Team.from_name('UNDER')

    @staticmethod
    def from_name(name):
        if Team.id_list is None or Team.abbr_dict is None:
            Team.init_class()

        abbr = team_name_convert(name)
        if abbr is None:
            return None

        return Team.abbr_dict[abbr]

    @staticmethod
    def group(group):
        if Team.id_list is None or Team.abbr_dict is None:
            Team.init_class()

        teams = []

        for team in Team.id_list:
            if team is not None and team.group == group:
                teams.append(team)

        return teams

    @staticmethod
    def all_teams(abbr_only=False):
        if Team.id_list is None or Team.abbr_dict is None:
            Team.init_class()

        teams = []

        for team in Team.id_list:
            if team is not None:
                if abbr_only:
                    teams.append(team.name)
                else:
                    teams.append(team)

        return teams

    @staticmethod
    def init_class():
        Team.id_list = [None,]
        Team.abbr_dict = {}

        rows = [
            ( 0, "Italy", "A", 1200),
            ( 1, "SLand", "A", 7000),
            ( 2, "Turkey", "A", 5000),
            ( 3, "Wales", "A", 10000),
            ( 4, "Belgium", "B", 600),
            ( 5, "Russia", "B", 10000),
            ( 6, "Denmark", "B", 2500),
            ( 7, "Finland", "B", 50000),
            ( 8, "Ukraine", "C", 10000),
            ( 9, "NLands", "C", 1100),
            (10, "Austria", "C", 10000),
            (11, "NMac", "C", 50000),
            (12, "England", "D", 550),
            (13, "Croatia", "D", 4000),
            (14, "CRep", "D", 15000),
            (15, "Scotland", "D", 30000),
            (16, "Spain", "E", 900),
            (17, "Poland", "E", 8000),
            (18, "Sweden", "E", 7500),
            (19, "Slovakia", "E", 30000),
            (20, "Germany", "F", 900),
            (21, "France", "F", 500),
            (22, "Portugal", "F", 800),
            (23, "Hungary", "F", 50000)
        ]

        for row in rows:
            team = Team.from_db(row)
            if team is not None:
                Team.id_list.append(team)
                Team.abbr_dict[team.name] = team

    @staticmethod
    def from_id(id):
        if Team.id_list is None or Team.abbr_dict is None:
            Team.init_class()
        
        return Team.id_list[id]

    @staticmethod
    def from_db(row):
        team = Team()

        team.team_id = row[0]
        team.name = row[1]
        team.group = row[2]
        team.odds = row[3]
        team.log_odds = math.log10(row[3])

        return team

    @staticmethod
    def from_ambig(input):
        if isinstance(input, Team):
            return input
        if isinstance(input, int):
            return Team.from_id(input)
        if isinstance(input, str):
            return Team.from_name(input)
        return None
