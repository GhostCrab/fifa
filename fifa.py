#!/usr/bin/python

from team import Team
from record import Record
from game import Game
from superRecord import SuperRecord

import argparse


def simulate_group(group):
    teams = Team.group(group)

    games = [
        Game(teams[0], teams[1], 0),
        Game(teams[0], teams[2], 0),
        Game(teams[0], teams[3], 0),
        Game(teams[1], teams[2], 0),
        Game(teams[1], teams[3], 0),
        Game(teams[2], teams[3], 0)
    ]

    return games

def simulate_tournament():
    all_games = []
    teams = Team.all_teams()
    records = {}
    elim = {"A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "X": []}

    for team in teams:
        records[team.name] = Record(team)
    
    for group in ["A", "B", "C", "D", "E", "F"]:
        all_games += simulate_group(group)

    for game in all_games:
        for team in game.teams:
            records[team.name].add(game)

    sorted_records = sorted(list(records.values()))

    for record in sorted_records:
        group = record.team.group
        elim[group].append(record.team)
        if len(elim["X"]) < 4:
            filled = False
            for x_team in elim["X"]:
                if x_team.group == group:
                    filled = True

            if not filled:
                elim["X"].append(record.team)

    # for record in sorted_records:
    #     print(record)

    elim["X"].sort(key=lambda x: x.group)
    xgroup_code = elim["X"][0].group + elim["X"][1].group + elim["X"][2].group + elim["X"][3].group

    # print("Group A: %10s %10s" % (elim["A"][0].name, elim["A"][1].name))
    # print("Group B: %10s %10s" % (elim["B"][0].name, elim["B"][1].name))
    # print("Group C: %10s %10s" % (elim["C"][0].name, elim["C"][1].name))
    # print("Group D: %10s %10s" % (elim["D"][0].name, elim["D"][1].name))
    # print("Group E: %10s %10s" % (elim["E"][0].name, elim["E"][1].name))
    # print("Group F: %10s %10s" % (elim["F"][0].name, elim["F"][1].name))
    # print("Extras:  %10s %10s %10s %10s [%s] " % (
    #     elim["X"][0].name, elim["X"][1].name, elim["X"][2].name, elim["X"][3].name, xgroup_code
    # ))

    # print("all games: %d" % (len(all_games)))

    # Round of 16
    if xgroup_code == "ABCD":
        all_games.append(Game(elim["A"][0], elim["C"][1], 1)) # Match 37
        all_games.append(Game(elim["A"][1], elim["B"][1], 1)) # Match 38
        all_games.append(Game(elim["B"][0], elim["A"][2], 1)) # Match 39
        all_games.append(Game(elim["C"][0], elim["D"][2], 1)) # Match 40
        all_games.append(Game(elim["F"][0], elim["C"][2], 1)) # Match 41
        all_games.append(Game(elim["D"][1], elim["E"][1], 1)) # Match 42
        all_games.append(Game(elim["E"][0], elim["B"][2], 1)) # Match 43
        all_games.append(Game(elim["D"][0], elim["F"][1], 1)) # Match 44
    elif xgroup_code == "ABCE":
        all_games.append(Game(elim["A"][0], elim["C"][1], 1)) # Match 37
        all_games.append(Game(elim["A"][1], elim["B"][1], 1)) # Match 38
        all_games.append(Game(elim["B"][0], elim["A"][2], 1)) # Match 39
        all_games.append(Game(elim["C"][0], elim["E"][2], 1)) # Match 40
        all_games.append(Game(elim["F"][0], elim["C"][2], 1)) # Match 41
        all_games.append(Game(elim["D"][1], elim["E"][1], 1)) # Match 42
        all_games.append(Game(elim["E"][0], elim["B"][2], 1)) # Match 43
        all_games.append(Game(elim["D"][0], elim["F"][1], 1)) # Match 44
    elif xgroup_code == "ABCF":
        all_games.append(Game(elim["A"][0], elim["C"][1], 1)) # Match 37
        all_games.append(Game(elim["A"][1], elim["B"][1], 1)) # Match 38
        all_games.append(Game(elim["B"][0], elim["A"][2], 1)) # Match 39
        all_games.append(Game(elim["C"][0], elim["F"][2], 1)) # Match 40
        all_games.append(Game(elim["F"][0], elim["C"][2], 1)) # Match 41
        all_games.append(Game(elim["D"][1], elim["E"][1], 1)) # Match 42
        all_games.append(Game(elim["E"][0], elim["B"][2], 1)) # Match 43
        all_games.append(Game(elim["D"][0], elim["F"][1], 1)) # Match 44
    elif xgroup_code == "ABDE":
        all_games.append(Game(elim["A"][0], elim["C"][1], 1)) # Match 37
        all_games.append(Game(elim["A"][1], elim["B"][1], 1)) # Match 38
        all_games.append(Game(elim["B"][0], elim["D"][2], 1)) # Match 39
        all_games.append(Game(elim["C"][0], elim["E"][2], 1)) # Match 40
        all_games.append(Game(elim["F"][0], elim["B"][2], 1)) # Match 41
        all_games.append(Game(elim["D"][1], elim["E"][1], 1)) # Match 42
        all_games.append(Game(elim["E"][0], elim["A"][2], 1)) # Match 43
        all_games.append(Game(elim["D"][0], elim["F"][1], 1)) # Match 44
    elif xgroup_code == "ABDF":
        all_games.append(Game(elim["A"][0], elim["C"][1], 1)) # Match 37
        all_games.append(Game(elim["A"][1], elim["B"][1], 1)) # Match 38
        all_games.append(Game(elim["B"][0], elim["D"][2], 1)) # Match 39
        all_games.append(Game(elim["C"][0], elim["F"][2], 1)) # Match 40
        all_games.append(Game(elim["F"][0], elim["B"][2], 1)) # Match 41
        all_games.append(Game(elim["D"][1], elim["E"][1], 1)) # Match 42
        all_games.append(Game(elim["E"][0], elim["A"][2], 1)) # Match 43
        all_games.append(Game(elim["D"][0], elim["F"][1], 1)) # Match 44
    elif xgroup_code == "ABEF":
        all_games.append(Game(elim["A"][0], elim["C"][1], 1)) # Match 37
        all_games.append(Game(elim["A"][1], elim["B"][1], 1)) # Match 38
        all_games.append(Game(elim["B"][0], elim["E"][2], 1)) # Match 39
        all_games.append(Game(elim["C"][0], elim["F"][2], 1)) # Match 40
        all_games.append(Game(elim["F"][0], elim["A"][2], 1)) # Match 41
        all_games.append(Game(elim["D"][1], elim["E"][1], 1)) # Match 42
        all_games.append(Game(elim["E"][0], elim["B"][2], 1)) # Match 43
        all_games.append(Game(elim["D"][0], elim["F"][1], 1)) # Match 44
    elif xgroup_code == "ACDE":
        all_games.append(Game(elim["A"][0], elim["C"][1], 1)) # Match 37
        all_games.append(Game(elim["A"][1], elim["B"][1], 1)) # Match 38
        all_games.append(Game(elim["B"][0], elim["E"][2], 1)) # Match 39
        all_games.append(Game(elim["C"][0], elim["D"][2], 1)) # Match 40
        all_games.append(Game(elim["F"][0], elim["A"][2], 1)) # Match 41
        all_games.append(Game(elim["D"][1], elim["E"][1], 1)) # Match 42
        all_games.append(Game(elim["E"][0], elim["C"][2], 1)) # Match 43
        all_games.append(Game(elim["D"][0], elim["F"][1], 1)) # Match 44
    elif xgroup_code == "ACDF":
        all_games.append(Game(elim["A"][0], elim["C"][1], 1)) # Match 37
        all_games.append(Game(elim["A"][1], elim["B"][1], 1)) # Match 38
        all_games.append(Game(elim["B"][0], elim["F"][2], 1)) # Match 39
        all_games.append(Game(elim["C"][0], elim["D"][2], 1)) # Match 40
        all_games.append(Game(elim["F"][0], elim["A"][2], 1)) # Match 41
        all_games.append(Game(elim["D"][1], elim["E"][1], 1)) # Match 42
        all_games.append(Game(elim["E"][0], elim["C"][2], 1)) # Match 43
        all_games.append(Game(elim["D"][0], elim["F"][1], 1)) # Match 44
    elif xgroup_code == "ACEF":
        all_games.append(Game(elim["A"][0], elim["C"][1], 1)) # Match 37
        all_games.append(Game(elim["A"][1], elim["B"][1], 1)) # Match 38
        all_games.append(Game(elim["B"][0], elim["E"][2], 1)) # Match 39
        all_games.append(Game(elim["C"][0], elim["F"][2], 1)) # Match 40
        all_games.append(Game(elim["F"][0], elim["A"][2], 1)) # Match 41
        all_games.append(Game(elim["D"][1], elim["E"][1], 1)) # Match 42
        all_games.append(Game(elim["E"][0], elim["C"][2], 1)) # Match 43
        all_games.append(Game(elim["D"][0], elim["F"][1], 1)) # Match 44
    elif xgroup_code == "ADEF":
        all_games.append(Game(elim["A"][0], elim["C"][1], 1)) # Match 37
        all_games.append(Game(elim["A"][1], elim["B"][1], 1)) # Match 38
        all_games.append(Game(elim["B"][0], elim["E"][2], 1)) # Match 39
        all_games.append(Game(elim["C"][0], elim["F"][2], 1)) # Match 40
        all_games.append(Game(elim["F"][0], elim["A"][2], 1)) # Match 41
        all_games.append(Game(elim["D"][1], elim["E"][1], 1)) # Match 42
        all_games.append(Game(elim["E"][0], elim["D"][2], 1)) # Match 43
        all_games.append(Game(elim["D"][0], elim["F"][1], 1)) # Match 44
    elif xgroup_code == "BCDE":
        all_games.append(Game(elim["A"][0], elim["C"][1], 1)) # Match 37
        all_games.append(Game(elim["A"][1], elim["B"][1], 1)) # Match 38
        all_games.append(Game(elim["B"][0], elim["E"][2], 1)) # Match 39
        all_games.append(Game(elim["C"][0], elim["D"][2], 1)) # Match 40
        all_games.append(Game(elim["F"][0], elim["C"][2], 1)) # Match 41
        all_games.append(Game(elim["D"][1], elim["E"][1], 1)) # Match 42
        all_games.append(Game(elim["E"][0], elim["B"][2], 1)) # Match 43
        all_games.append(Game(elim["D"][0], elim["F"][1], 1)) # Match 44
    elif xgroup_code == "BCDF":
        all_games.append(Game(elim["A"][0], elim["C"][1], 1)) # Match 37
        all_games.append(Game(elim["A"][1], elim["B"][1], 1)) # Match 38
        all_games.append(Game(elim["B"][0], elim["F"][2], 1)) # Match 39
        all_games.append(Game(elim["C"][0], elim["D"][2], 1)) # Match 40
        all_games.append(Game(elim["F"][0], elim["B"][2], 1)) # Match 41
        all_games.append(Game(elim["D"][1], elim["E"][1], 1)) # Match 42
        all_games.append(Game(elim["E"][0], elim["C"][2], 1)) # Match 43
        all_games.append(Game(elim["D"][0], elim["F"][1], 1)) # Match 44
    elif xgroup_code == "BCEF":
        all_games.append(Game(elim["A"][0], elim["C"][1], 1)) # Match 37
        all_games.append(Game(elim["A"][1], elim["B"][1], 1)) # Match 38
        all_games.append(Game(elim["B"][0], elim["F"][2], 1)) # Match 39
        all_games.append(Game(elim["C"][0], elim["E"][2], 1)) # Match 40
        all_games.append(Game(elim["F"][0], elim["B"][2], 1)) # Match 41
        all_games.append(Game(elim["D"][1], elim["E"][1], 1)) # Match 42
        all_games.append(Game(elim["E"][0], elim["C"][2], 1)) # Match 43
        all_games.append(Game(elim["D"][0], elim["F"][1], 1)) # Match 44
    elif xgroup_code == "BDEF":
        all_games.append(Game(elim["A"][0], elim["C"][1], 1)) # Match 37
        all_games.append(Game(elim["A"][1], elim["B"][1], 1)) # Match 38
        all_games.append(Game(elim["B"][0], elim["F"][2], 1)) # Match 39
        all_games.append(Game(elim["C"][0], elim["E"][2], 1)) # Match 40
        all_games.append(Game(elim["F"][0], elim["B"][2], 1)) # Match 41
        all_games.append(Game(elim["D"][1], elim["E"][1], 1)) # Match 42
        all_games.append(Game(elim["E"][0], elim["D"][2], 1)) # Match 43
        all_games.append(Game(elim["D"][0], elim["F"][1], 1)) # Match 44
    elif xgroup_code == "CDEF":
        all_games.append(Game(elim["A"][0], elim["C"][1], 1)) # Match 37
        all_games.append(Game(elim["A"][1], elim["B"][1], 1)) # Match 38
        all_games.append(Game(elim["B"][0], elim["F"][2], 1)) # Match 39
        all_games.append(Game(elim["C"][0], elim["E"][2], 1)) # Match 40
        all_games.append(Game(elim["F"][0], elim["C"][2], 1)) # Match 41
        all_games.append(Game(elim["D"][1], elim["E"][1], 1)) # Match 42
        all_games.append(Game(elim["E"][0], elim["D"][2], 1)) # Match 43
        all_games.append(Game(elim["D"][0], elim["F"][1], 1)) # Match 44

    # Quarter-finals
    all_games.append(Game(all_games[40].winner, all_games[41].winner, 2)) # Match 45
    all_games.append(Game(all_games[38].winner, all_games[36].winner, 2)) # Match 46
    all_games.append(Game(all_games[39].winner, all_games[37].winner, 2)) # Match 47
    all_games.append(Game(all_games[42].winner, all_games[43].winner, 2)) # Match 48

    # Semi-finals
    all_games.append(Game(all_games[45].winner, all_games[44].winner, 3)) # Match 49
    all_games.append(Game(all_games[47].winner, all_games[46].winner, 3)) # Match 50

    # Final
    all_games.append(Game(all_games[48].winner, all_games[49].winner, 4)) # Match 51

    return all_games


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', '--debug', action='store_true')
    args = parser.parse_args()

    if args.debug:
        print("Debug")

    teams = Team.all_teams()
    super_records = {}
    for team in teams:
        super_records[team.name] = SuperRecord(team)

    runs = 50000
    for i in range(runs):
        print("%.2f%%" % (i/runs*100), end='\r')
        all_games = simulate_tournament()

        records = {}
        for team in teams:
            records[team.name] = Record(team)

        for game in all_games:
            for team in game.teams:
                records[team.name].add(game)

        for team in teams:
            super_records[team.name].collect(records[team.name])

    sorted_records = sorted(list(super_records.values()))

    for record in sorted_records:
        print(record)

    # final_records = {"A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "X": []}

    # for record in sorted_records:
    #     group = record.team.group
    #     final_records[group].append(record.team)

    # print("Results: ")
    # for group in ["A", "B", "C", "D", "E", "F"]:
    #     print("  Group %s: " % (group))
    #     for team in final_records[group]:
    #         print(records[team.name])
