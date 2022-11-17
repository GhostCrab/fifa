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
        return "(%02d) %10s %s %5d %.2f" % (self.team_id, self.name, self.group, self.odds, self.log_odds)

    def __eq__(self, other):
        o = Team.from_ambig(other)
        if o is not None:
            return self.team_id == o.team_id
        return NotImplemented

    def __lt__(self, other):
        #print("Comparing %s < %s" % (self.team, other.team))
        if self.odds < other.odds:
            return True
        elif self.odds > other.odds:
            return False

        if self.team_id < other.team_id:
            return True

        return False

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

        # abbr = team_name_convert(name)
        # if abbr is None:
        #     return None

        return Team.abbr_dict[name.upper()]

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
            ( 0, "QATAR", "A", 25000),
            ( 1, "ECUADOR", "A", 15000),
            ( 2, "SENEGAL", "A", 12500),
            ( 3, "NETHERLANDS", "A", 1200),
            ( 4, "ENGLAND", "B", 800),
            ( 5, "IRAN", "B", 50000),
            ( 6, "USA", "B", 15000),
            ( 7, "WALES", "B", 20000),
            ( 8, "ARGENTINA", "C", 550),
            ( 9, "SAUDI ARABIA", "C", 75000),
            (10, "MEXICO", "C", 15000),
            (11, "POLAND", "C", 15000),
            (12, "FRANCE", "D", 600),
            (13, "AUSTRLIA", "D", 35000),
            (14, "DENMARK", "D", 2800),
            (15, "TUNISIA", "D", 50000),
            (16, "SPAIN", "E", 850),
            (17, "COSTA RICA", "E", 75000),
            (18, "GERMANY", "E", 1000),
            (19, "JAPAN", "E", 25000),
            (20, "BELGIUM", "F", 1600),
            (21, "CANADA", "F", 20000),
            (22, "MOROCCO", "F", 20000),
            (23, "CROATIA", "F", 5000),
            (24, "BRAZIL", "G", 400),
            (25, "SERBIA", "G", 8000),
            (26, "SWITZERLAND", "G", 10000),
            (27, "CAMEROON", "G", 25000),
            (28, "PORTUGAL", "H", 1400),
            (29, "GHANA", "H", 25000),
            (30, "URUGUAY", "H", 5000),
            (31, "KOREA", "H", 25000),
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
