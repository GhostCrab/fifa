#!/usr/bin/python

from team import Team
from record import Record
from game import Game
from draft import Draft
from superRecord import SuperRecord

import argparse
import numpy as np
import random

def simulate_draft(drafts, teams):
    draft_teams = teams.copy()
    for i in [0,1,2,3,4,5,5,4,3,2,1,0,0,1,2,3,4,5,5,4,3,2,1,0,0,1,2,3,4,5]:
        pick_index = round(abs(np.random.normal(0, 2)))
        if pick_index >= len(draft_teams):
            pick_index = len(draft_teams) - 1

        # print("%s drafting #%d (%s)" % (drafts[i].player, pick_index, draft_teams[pick_index]))
        drafts[i].add_team(draft_teams.pop(pick_index))

def get_draft():
    drafts = [
        Draft("Andrew"),
        Draft("Bardia"),
        Draft("Cooper"),
        Draft("Micah"),
        Draft("Ryan"),
        Draft("TJ"),
    ]
    drafts[0].add_team(Team.from_name("France"))
    drafts[0].add_team(Team.from_name("USA"))
    drafts[0].add_team(Team.from_name("Wales"))
    drafts[0].add_team(Team.from_name("Japan"))

    drafts[1].add_team(Team.from_name("Netherlands"))
    drafts[1].add_team(Team.from_name("German"))
    drafts[1].add_team(Team.from_name("Iran"))
    drafts[1].add_team(Team.from_name("Ghana"))

    drafts[2].add_team(Team.from_name("England"))
    drafts[2].add_team(Team.from_name("Senegal"))
    drafts[2].add_team(Team.from_name("Uruguay"))
    drafts[2].add_team(Team.from_name("Korea"))

    drafts[3].add_team(Team.from_name("Spain"))
    drafts[3].add_team(Team.from_name("Belgium"))
    drafts[3].add_team(Team.from_name("Switzerland"))
    drafts[3].add_team(Team.from_name("Poland"))

    drafts[4].add_team(Team.from_name("Brazil"))
    drafts[4].add_team(Team.from_name("Denmark"))
    drafts[4].add_team(Team.from_name("Croatia"))
    drafts[4].add_team(Team.from_name("Ecuador"))

    drafts[5].add_team(Team.from_name("Argentina"))
    drafts[5].add_team(Team.from_name("Portugal"))
    drafts[5].add_team(Team.from_name("Mexico"))
    drafts[5].add_team(Team.from_name("Canada"))
    

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
    elim = {"A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "G": [], "H": []}

    for team in teams:
        records[team.name] = Record(team)
    
    for group in ["A", "B", "C", "D", "E", "F", "G", "H"]:
        all_games += simulate_group(group)

    for game in all_games:
        for team in game.teams:
            records[team.name].add(game)

    sorted_records = sorted(list(records.values()))

    for record in sorted_records:
        group = record.team.group
        elim[group].append(record.team)

    # for record in sorted_records:
    #     print(record)

    # print("Group A: %10s %10s" % (elim["A"][0].name, elim["A"][1].name))
    # print("Group B: %10s %10s" % (elim["B"][0].name, elim["B"][1].name))
    # print("Group C: %10s %10s" % (elim["C"][0].name, elim["C"][1].name))
    # print("Group D: %10s %10s" % (elim["D"][0].name, elim["D"][1].name))
    # print("Group E: %10s %10s" % (elim["E"][0].name, elim["E"][1].name))
    # print("Group F: %10s %10s" % (elim["F"][0].name, elim["F"][1].name))
    # print("Group F: %10s %10s" % (elim["G"][0].name, elim["G"][1].name))
    # print("Group F: %10s %10s" % (elim["H"][0].name, elim["H"][1].name))

    # print("all games: %d" % (len(all_games)))

    # Round of 16
    all_games.append(Game(elim["A"][0], elim["B"][1], 1)) # Match 48
    all_games.append(Game(elim["C"][0], elim["D"][1], 1)) # Match 49
    all_games.append(Game(elim["D"][0], elim["C"][1], 1)) # Match 50
    all_games.append(Game(elim["B"][0], elim["A"][1], 1)) # Match 51
    all_games.append(Game(elim["E"][0], elim["F"][1], 1)) # Match 52
    all_games.append(Game(elim["G"][0], elim["H"][1], 1)) # Match 53
    all_games.append(Game(elim["F"][0], elim["E"][1], 1)) # Match 54
    all_games.append(Game(elim["H"][0], elim["G"][1], 1)) # Match 55

    # Quarter-finals
    all_games.append(Game(all_games[52].winner, all_games[53].winner, 2)) # Match 56
    all_games.append(Game(all_games[48].winner, all_games[49].winner, 2)) # Match 57
    all_games.append(Game(all_games[54].winner, all_games[55].winner, 2)) # Match 58
    all_games.append(Game(all_games[50].winner, all_games[51].winner, 2)) # Match 59

    # Semi-finals
    all_games.append(Game(all_games[56].winner, all_games[57].winner, 3)) # Match 60
    all_games.append(Game(all_games[58].winner, all_games[59].winner, 3)) # Match 61

    # Final
    all_games.append(Game(all_games[60].winner, all_games[61].winner, 4)) # Match 62

    # index = 0
    # for game in all_games:
    #     print("%d: %s" % (index, game))
    #     index += 1

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

    runs = 1000
    for i in range(runs):
        print("Tournament Simulation: %.2f%%" % (i/runs*100), end='\r')
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

    for team in teams:
        team.value = super_records[team.name].points(0)["mean"]

    sorted_teams = sorted(teams)
    for index, team in enumerate(sorted_teams):
        print("%2d %s [%5.2f]" % (index+1, team, super_records[team.name].points(0)["mean"]))

    player_ranks = [[],[],[],[],[],[]]

    draft_runs = 1
    for i in range(draft_runs):
        print("Draft Simulation: %.2f%%" % (i/draft_runs*100), end='\r')
        # drafts = [
            # Draft(0),
            # Draft(1),
            # Draft(2),
            # Draft(3),
            # Draft(4),
            # Draft(5)
        # ]
# 
        # simulate_draft(drafts, sorted_teams)
        drafts = get_draft()
        for draft in drafts:
            draft.add_records(super_records.values())

        sorted_drafts = sorted(drafts)
        for i, draft in enumerate(sorted_drafts):
            player_ranks[draft.player].append(i)
            # print(draft)

    for player, ranks in enumerate(player_ranks):
        print("Player %d: %.2f %.2f %.2f %.2f %.2f %.2f %.2f" % (
            player,
            np.mean(ranks),
            ranks.count(0) / draft_runs,
            ranks.count(1) / draft_runs,
            ranks.count(2) / draft_runs,
            ranks.count(3) / draft_runs,
            ranks.count(4) / draft_runs,
            ranks.count(5) / draft_runs,
        ))

    # final_records = {"A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "X": []}

    # for record in sorted_records:
    #     group = record.team.group
    #     final_records[group].append(record.team)

    # print("Results: ")
    # for group in ["A", "B", "C", "D", "E", "F"]:
    #     print("  Group %s: " % (group))
    #     for team in final_records[group]:
    #         print(records[team.name])
