#!/usr/bin/python

import random
import numpy as np

class Game():
    def __init__(self, team_1, team_2, stage):
        self.teams = [team_1, team_2]
        if (team_1.log_odds >= team_2.log_odds):
            self.teams = [team_2, team_1]

        self._score = None
        self._raw_score = None
        self._winner = None
        self.stage = stage

    def __str__(self):
        # return "%10s: %d %10s: %d   Winner: %-10s (%.2f %.2f %.2f; %.2f %.2f)" % (
        #     self.teams[0].name, score[0], 
        #     self.teams[1].name, score[1], 
        #     self.winner.name, 
        #     self.teams[0].log_odds, self.teams[1].log_odds, 
        #     -(self.teams[0].log_odds - self.teams[1].log_odds), 
        #     self._score[0], self._score[1]
        # )

        return "%10s: %d %10s: %d   Winner: %-10s" % (
            self.teams[0].name, self.score[0], 
            self.teams[1].name, self.score[1], 
            self.winner.name
        )

    @property
    def score(self):
        if self._score is None:
            self._raw_score = [-(self.teams[0].log_odds - self.teams[1].log_odds),0]

            self._raw_score += np.random.normal(0.5, 0.5, 2)

            if self._raw_score[0] < 0:
                self._raw_score[1] -= self._raw_score[0]
                self._raw_score[0] = 0

            if self._raw_score[1] < 0:
                self._raw_score[0] -= self._raw_score[1]
                self._raw_score[1] = 0

            self._score = (round(self._raw_score[0]), round(self._raw_score[1]))

        return self._score

    @property
    def winner(self):
        if self._winner is None:
            score = self.score
            if score[0] == score[1]:
                self._winner = self.teams[random.randint(0,1)]
            elif score[0] > score[1]:
                self._winner = self.teams[0]
            else:
                self._winner = self.teams[1]

        return self._winner

    def stat(self, team):
        if team not in self.teams:
            return None

        score = self.score
        win = self.winner == team
        pk = self.score[0] == self.score[1]
        if team == self.teams[0]:
            return (win, pk, self.score[0], self.score[1], self.teams[1])
        if team == self.teams[1]:
            return (win, pk, self.score[1], self.score[0], self.teams[0])
