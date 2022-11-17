#!/usr/bin/python

import numpy as np

class SuperRecord():
    def __init__(self, team):
        self.team = team
        self._total_wins = []
        self._total_losses = []
        self._pk_wins = []
        self._pk_losses = []
        self._group_wins = []
        self._group_losses = []
        self._group_ties = []
        self._elim_wins = []
        self.eliminated = [0, 0, 0, 0, 0, 0]
        self._goals_scored = []
        self._goals_allowed = []
        self._points = [[], [], [], []]

    @property
    def goal_differential(self):
        return self.goals_scored["mean"] - self.goals_allowed["mean"]

    @property
    def total_wins(self):
        return {"mean": np.mean(self._total_wins), "std": np.std(self._total_wins), "var": np.var(self._total_wins)}

    @property
    def total_losses(self):
        return {"mean": np.mean(self._total_losses), "std": np.std(self._total_losses), "var": np.var(self._total_losses)}

    @property
    def pk_wins(self):
        return {"mean": np.mean(self._pk_wins), "std": np.std(self._pk_wins), "var": np.var(self._pk_wins)}

    @property
    def pk_losses(self):
        return {"mean": np.mean(self._pk_losses), "std": np.std(self._pk_losses), "var": np.var(self._pk_losses)}

    @property
    def group_wins(self):
        return {"mean": np.mean(self._group_wins), "std": np.std(self._group_wins), "var": np.var(self._group_wins)}

    @property
    def group_losses(self):
        return {"mean": np.mean(self._group_losses), "std": np.std(self._group_losses), "var": np.var(self._group_losses)}

    @property
    def group_ties(self):
        return {"mean": np.mean(self._group_ties), "std": np.std(self._group_ties), "var": np.var(self._group_ties)}

    @property
    def elim_wins(self):
        return {"mean": np.mean(self._elim_wins), "std": np.std(self._elim_wins), "var": np.var(self._elim_wins)}

    @property
    def goals_scored(self):
        return {"mean": np.mean(self._goals_scored), "std": np.std(self._goals_scored), "var": np.var(self._goals_scored)}

    @property
    def goals_allowed(self):
        return {"mean": np.mean(self._goals_allowed), "std": np.std(self._goals_allowed), "var": np.var(self._goals_allowed)}

    @property
    def elim_str(self):
        count = len(self._total_wins)
        estr = "Eliminated in round 0: %.2f 1: %.2f 2: %.2f 3:%.2f 4:%.2f C:%.2f" % (
            self.eliminated[0] / count * 100,
            self.eliminated[1] / count * 100,
            self.eliminated[2] / count * 100,
            self.eliminated[3] / count * 100,
            self.eliminated[4] / count * 100,
            self.eliminated[5] / count * 100,
        )

        return estr

    def __str__(self):
        return "    %s (%d) %.2f %.2f %.2f %.2f:\n      Record: %.2f-%.2f-%.2f [PKs: %.2f-%.2f]\n      Group: %.2f-%.2f-%.2f\n      Eliminated: %s\n      Goals: %.2f-%.2f [%.2f]" % (
            self.team.name, self.team.odds, 
            self.points(0)["mean"], self.points(1)["mean"], self.points(2)["mean"], self.points(3)["mean"],
            self.total_wins["mean"], self.total_losses["mean"], self.group_ties["mean"],
            self.pk_wins["mean"], self.pk_losses["mean"],
            self.group_wins["mean"], self.group_losses["mean"], self.group_ties["mean"],
            self.elim_str,
            self.goals_scored["mean"], self.goals_allowed["mean"], self.goal_differential
        )

    def __lt__(self, other):
        #print("Comparing %s < %s" % (self.team, other.team))
        if self.points(0)["mean"] > other.points(0)["mean"]:
            return True
        elif self.points(0)["mean"] < other.points(0)["mean"]:
            return False

        if self.total_wins["mean"] > other.total_wins["mean"]:
            return True
        elif self.total_wins["mean"] < other.total_wins["mean"]:
            return False

        if self.goal_differential > other.goal_differential:
            return True
        elif self.goal_differential < other.goal_differential:
            return False

        if self.goals_scored["mean"] > other.goals_scored["mean"]:
            return True
        elif self.goals_scored["mean"] < other.goals_scored["mean"]:
            return False

        if self.team.odds < other.team.odds:
            return True
        elif self.team.odds > other.team.odds:
            return False

        if self.team.team_id < other.team.team_id:
            return True
        elif self.team.team_id > other.team.team_id:
            return False

        return False

    def points(self, points_type):
        #return {"mean": np.mean(self._points[points_type]), "std": np.std(self._points[points_type]), "var": np.var(self._points[points_type])}
        return {"mean": np.mean(self._points[points_type])}

    def collect(self, record):
        if self.team != record.team:
            return

        self._total_wins.append(record.total_wins)
        self._total_losses.append(record.total_losses)
        self._pk_wins.append(record.pk_wins)
        self._pk_losses.append(record.pk_losses)
        self._group_wins.append(record.group_wins)
        self._group_losses.append(record.group_losses)
        self._group_ties.append(record.group_ties)
        self._elim_wins.append(record.elim_wins)
        self.eliminated[record.eliminated] += 1
        self._goals_scored.append(record.goals_scored)
        self._goals_allowed.append(record.goals_allowed)
        for i in range(len(self._points)):
            self._points[i].append(record.points(i))