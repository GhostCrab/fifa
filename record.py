#!/usr/bin/python

class Record():
    def __init__(self, team):
        self.team = team
        self.games = []
        self.total_wins = 0
        self.total_losses = 0
        self.pk_wins = 0
        self.pk_losses = 0
        self.group_wins = 0
        self.group_ties = 0
        self.group_losses = 0
        self.elim_wins = 0
        self.eliminated = 0
        self.champ = False
        self.goals_scored = 0
        self.goals_allowed = 0
        self.pts = 0

    @property
    def goal_differential(self):
        return self.goals_scored - self.goals_allowed

    def __str__(self):
        group_stats = []
        for i in range(3):
            group_stats.append(self.games[i].stat(self.team))

        group_string = ""
        for stat in group_stats:
            (win, pk, pts, gs, ga, ot) = stat
            if win is None:
                group_string += "%s %d-%d [T]; " % (ot.name, gs, ga)
            else:
                group_string += "%s %d-%d [%s]; " % (ot.name, gs, ga, "W" if win else "L")

        elim_stats = []
        for i in range(3,7):
            if i < len(self.games):
                elim_stats.append(self.games[i].stat(self.team))

        elim_string = ""
        for stat in elim_stats:
            (win, pk, pts, gs, ga, ot) = stat
            if pk:
                elim_string += "%s %d-%d [%s-PK]; " % (ot.name, gs, ga, "W" if win else "L")
            else:
                elim_string += "%s %d-%d [%s]; " % (ot.name, gs, ga, "W" if win else "L")

        champ_string = ""
        if self.champ:
            champ_string = " *CHAMP*"

        return "    %s (%d)%s:\n      Record: %d-%d [PKs: %d-%d]\n      Group: %d-%d-%d - %s\n      Eliminated: %s%s%s\n      Goals: %d-%d [%d]\n      Points: %d" % (
            self.team.name, self.team.odds, champ_string,
            self.total_wins, self.total_losses,
            self.pk_wins, self.pk_losses,
            self.group_wins, self.group_losses, self.group_ties, group_string,
            self.eliminated if not self.champ else "-- ", " - " if self.eliminated > 0 and self.eliminated < 5 else "", elim_string,
            self.goals_scored, self.goals_allowed, self.goal_differential,
            self.points(0)
        )

    def __lt__(self, other):
        if self.pts > other.pts:
            return True
        elif self.pts < other.pts:
            return False

        # gde = self.goal_differential_exclusive(other.team)
        # if gde > 0:
        #     return True
        # elif gde < 0:
        #     return False

        if self.goal_differential > other.goal_differential:
            return True
        elif self.goal_differential < other.goal_differential:
            return False

        wde = self.win_differential_exclusive(other.team)
        if wde > 0:
            return True
        elif wde < 0:
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

    def goal_differential_exclusive(self, team):
        gd = 0
        for game in self.games:
            stat = game.stat(team)
            if stat is not None:
                (win, pk, pts, gs, ga, ot) = stat
                if stat[0]:
                    gd += ga - gs

        return gd

    def win_differential_exclusive(self, team):
        wd = 0
        for game in self.games:
            stat = game.stat(team)
            if stat is not None:
                if stat[0] is None:
                    pass
                elif stat[0]:
                    wd -= 1
                else:
                    wd += 1

        return wd

    def add(self, game):
        stat = game.stat(self.team)
        if stat is None:
            print("Tried to add %s to %s's record")
            return

        self.games.append(game)

        (win, pk, pts, gs, ga, ot) = stat

        self.goals_scored += gs
        self.goals_allowed += ga
        self.pts += pts

        if win:
            self.total_wins += 1

            if game.stage == 0:
                self.group_wins += 1
            else:
                self.elim_wins += 1

            if game.stage == 4:
                self.champ = True
                self.eliminated = 5

            if pk:
                self.pk_wins += 1
        elif win is None: # loss
            self.group_ties += 1
        else:
            self.total_losses += 1

            if game.stage == 0:
                self.group_losses += 1
            else:
                self.eliminated = game.stage

            if pk:
                self.pk_losses += 1

    def points(self, points_type):
        knockout_wins = self.total_wins - self.group_wins

        special_points = (self.group_wins * 3) + (self.group_ties * 1) + (1 if self.eliminated > 0 else 0)
        for game in self.games:
            if game.stage > 0:
                stat = game.stat(self.team)
                (win, pk, pts, gs, ga, ot) = stat
                if win:
                    special_points += 3 + game.stage
        if points_type == 1: # 3 points for a win, 1 point for a draw in group
            return self.pts
        if points_type == 0: # 3 points for a win, +1 if champ win, +1 to make it past elimination
            return (self.pts) + (1 if self.champ else 0) + (1 if self.eliminated > 0 else 0)
            #return (self.pts) + (1 if self.champ else 0) + (1 if self.eliminated > 0 else 0) + knockout_wins
            #return knockout_wins
        if points_type == 2: # win = 3, pk win = 2, pk loss = 1
            clean_wins = self.total_wins - self.pk_wins
            return self.pts + (self.pk_wins * -1) + (self.pk_losses)
        if points_type == 3: # win = 3, pk win = 2, pk loss = 1, +1 for champ win, +1 to make it past elimination
            clean_wins = self.total_wins - self.pk_wins
            return self.pts + (self.pk_wins * -1) + (self.pk_losses) + (1 if self.champ else 0) + (1 if self.eliminated > 0 else 0)




    def points(self, points_type):
        if points_type == 1: # 3 points for a win, 1 point for a draw in group
            return self.pts
        if points_type == 0: # 3 points for a win, +1 if champ win, +1 to make it past elimination
            return (self.pts) + (1 if self.champ else 0) + (1 if self.eliminated > 0 else 0)
        if points_type == 2: # win = 3, pk win = 2, pk loss = 1
            clean_wins = self.total_wins - self.pk_wins
            return self.pts + (self.pk_wins * -1) + (self.pk_losses)
        if points_type == 3: # win = 3, pk win = 2, pk loss = 1, +1 for champ win, +1 to make it past elimination
            clean_wins = self.total_wins - self.pk_wins
            return self.pts + (self.pk_wins * -1) + (self.pk_losses) + (1 if self.champ else 0) + (1 if self.eliminated > 0 else 0)