#!/usr/bin/python

class SuperRecord():
    def __init__(self, team):
        self.team = team
        self.count = 0
        self.total_wins = 0
        self.total_losses = 0
        self.pk_wins = 0
        self.pk_losses = 0
        self.group_wins = 0
        self.group_losses = 0
        self.elim_wins = 0
        self.eliminated = [0, 0, 0, 0, 0, 0]
        self.goals_scored = 0
        self.goals_allowed = 0

    @property
    def goal_differential(self):
        return self.goals_scored - self.goals_allowed

    @property
    def elim_str(self):
        estr = "Eliminated in round 0: %.2f 1: %.2f 2: %.2f 3:%.2f 4:%.2f C:%.2f" % (
            self.eliminated[0] / self.count * 100,
            self.eliminated[1] / self.count * 100,
            self.eliminated[2] / self.count * 100,
            self.eliminated[3] / self.count * 100,
            self.eliminated[4] / self.count * 100,
            self.eliminated[5] / self.count * 100,
        )

        return estr


    def __str__(self):
        return "    %s (%d) %.2f:\n      Record: %d-%d [PKs: %d-%d]\n      Group: %d-%d\n      Eliminated: %s\n      Goals: %d-%d [%d]" % (
            self.team.name, self.team.odds, self.total_wins / self.count,
            self.total_wins, self.total_losses,
            self.pk_wins, self.pk_losses,
            self.group_wins, self.group_losses,
            self.elim_str,
            self.goals_scored, self.goals_allowed, self.goal_differential
        )

    def __lt__(self, other):
        #print("Comparing %s < %s" % (self.team, other.team))
        if self.total_wins > other.total_wins:
            return True
        elif self.total_wins < other.total_wins:
            return False

        if self.goal_differential > other.goal_differential:
            return True
        elif self.goal_differential < other.goal_differential:
            return False

        if self.goals_scored > other.goals_scored:
            return True
        elif self.goals_scored < other.goals_scored:
            return False

        if self.team.odds < other.team.odds:
            return True
        elif self.team.odds > other.team.odds:
            return False

        if self.team.team_id < self.team.team_id:
            return True
        elif self.team.team_id > self.team.team_id:
            return False

        return False

    def collect(self, record):
        if self.team != record.team:
            return

        self.count += 1

        self.total_wins += record.total_wins
        self.total_losses += record.total_losses
        self.pk_wins += record.pk_wins
        self.pk_losses += record.pk_losses
        self.group_wins += record.group_wins
        self.group_losses += record.group_losses
        self.elim_wins += record.elim_wins
        self.eliminated[record.eliminated] += 1
        self.goals_scored += record.goals_scored
        self.goals_allowed += record.goals_allowed