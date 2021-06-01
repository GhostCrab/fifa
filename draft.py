#!/usr/bin/python

from superRecord import SuperRecord

class Draft():
    def __init__(self, player):
        self.player = player
        self.teams = []
        self.records = []

    def ___str__(self):
        records = [
            self.get_record_by_team(self.teams[0]),
            self.get_record_by_team(self.teams[1]),
            self.get_record_by_team(self.teams[2]),
            self.get_record_by_team(self.teams[3])
        ]
        return ("Player %d:\n  %s: %.2f %.2f %.2f %.2f\n  %s: %.2f %.2f %.2f %.2f\n  %s: %.2f %.2f %.2f %.2f\n  %s: %.2f %.2f %.2f %.2f\n  Total: %.2f %.2f %.2f %.2f" % (
            self.player,
            self.teams[0].name, records[0].points(0)["mean"], records[0].points(1)["mean"], records[0].points(2)["mean"], records[0].points(3)["mean"],
            self.teams[1].name, records[1].points(0)["mean"], records[1].points(1)["mean"], records[1].points(2)["mean"], records[1].points(3)["mean"],
            self.teams[2].name, records[2].points(0)["mean"], records[2].points(1)["mean"], records[2].points(2)["mean"], records[2].points(3)["mean"],
            self.teams[3].name, records[3].points(0)["mean"], records[3].points(1)["mean"], records[3].points(2)["mean"], records[3].points(3)["mean"],
            self.score(0), self.score(1), self.score(2), self.score(3),
        ))

    def __str__(self):

        return ("Player %d: %.2f %.2f %.2f %.2f [%10s, %10s, %10s, %10s]" % (
            self.player,
            self.score(0), self.score(1), self.score(2), self.score(3),
            self.teams[0].name,
            self.teams[1].name,
            self.teams[2].name,
            self.teams[3].name,
        ))

    def __lt__(self, other):
        if self.score(0) > other.score(0):
            return True
        elif self.score(0) < other.score(0):
            return False

        if self.score(1) > other.score(1):
            return True
        elif self.score(1) < other.score(1):
            return False

        if self.score(2) > other.score(2):
            return True
        elif self.score(2) < other.score(2):
            return False

        if self.score(3) > other.score(3):
            return True
        elif self.score(3) < other.score(3):
            return False

        return False

    def get_record_by_team(self, team):
        for record in self.records:
            if record.team == team:
                return record

        return None

    def add_team(self, team):
        self.teams.append(team)

    def add_records(self, records):
        for record in records:
            if record.team in self.teams:
                self.records.append(record)

    def score(self, points_type):
        score = 0
        for record in self.records:
            score += record.points(points_type)["mean"]

        return score

