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
    for i in [0,1,2,3,4,5,5,4,3,2,1,0,0,1,2,3,4,5,5,4,3,2,1,0]:
        pick_index = round(abs(np.random.normal(0, 2)))
        if pick_index >= len(draft_teams):
            pick_index = len(draft_teams) - 1

        #print("%s drafting #%d (%s)" % (drafts[i].player, pick_index, draft_teams[pick_index]))
        drafts[i].add_team(draft_teams.pop(pick_index))

def true_draft():
    return [
        Draft("ANDREW", Team.from_name("France"), Team.from_name("USA"), Team.from_name("Wales"), Team.from_name("Japan")),
        Draft("BARDIA", Team.from_name("Netherlands"), Team.from_name("Germany"), Team.from_name("Iran"), Team.from_name("Ghana")),
        Draft("COOPER", Team.from_name("England"), Team.from_name("Senegal"), Team.from_name("Uruguay"), Team.from_name("Korea")),
        Draft("MICAH",  Team.from_name("Spain"), Team.from_name("Belgium"), Team.from_name("Switzerland"), Team.from_name("Poland")),
        Draft("RYAN",   Team.from_name("Brazil"), Team.from_name("Denmark"), Team.from_name("Croatia"), Team.from_name("Ecuador")),
        Draft("TJ",     Team.from_name("Argentina"), Team.from_name("Portugal"), Team.from_name("Mexico"), Team.from_name("Canada"))
    ]

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


def real_tournament(modifier=None):
    all_games = []
    teams = Team.all_teams()
    records = {}
    elim = {"A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "X": []}
    elim_records = {"A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "X": []}

    for team in teams:
        records[team.name] = Record(team)

    Austria = Team.from_name("Austria")      # 18 Austria  C 10000  5.08 ANDREW  +4 QUALIFIED
    Belgium = Team.from_name("Belgium")      #  3 Belgium  B   600 14.05 COOPER  +0 QUALIFIED
    Croatia = Team.from_name("Croatia")      # 10 Croatia  D  4000  7.67 MICAH   +0 QUALIFIED
    CzecRep = Team.from_name("CzecRep")      # 19 CzecRep  D 15000  3.44 RYAN    +1 QUALIFIED
    Denmark = Team.from_name("Denmark")      #  9 Denmark  B  2500  8.88 COOPER  +0 QUALIFIED
    England = Team.from_name("England")      #  2 England  D   550 13.11 TJ      +0 QUALIFIED
    Finland = Team.from_name("Finland")      # 22 Finland  B 50000  0.85 ANDREW  +1
    France = Team.from_name("France")        #  1 France   F   500 12.64 ANDREW  +0 QUALIFIED
    Germany = Team.from_name("Germany")      #  6 Germany  F   900  8.99 BARDIA  +0 QUALIFIED
    Hungary = Team.from_name("Hungary")      # 24 Hungary  F 50000  0.12 COOPER  +2
    Italy = Team.from_name("Italy")          #  8 Italy    A  1200 11.53 RYAN    +1 QUALIFIED
    NLands = Team.from_name("NLands")        #  7 NLands   C  1100 13.59 RYAN    +1 QUALIFIED
    NorthMac = Team.from_name("NorthMac")    # 23 NorthMac C 50000  1.29 MICAH   +2
    Poland = Team.from_name("Poland")        # 14 Poland   E  8000  5.24 ANDREW  +3
    Portugal = Team.from_name("Portugal")    #  4 Portugal F   800  9.68 BARDIA  +0 QUALIFIED
    Russia = Team.from_name("Russia")        # 16 Russia   B 10000  4.15 MICAH   +2
    Scotland = Team.from_name("Scotland")    # 20 Scotland D 30000  1.73 BARDIA  +0
    Slovakia = Team.from_name("Slovakia")    # 21 Slovakia E 30000  1.59 TJ      +0
    Spain = Team.from_name("Spain")          #  5 Spain    E   900 13.29 MICAH   +1 QUALIFIED
    Sweden = Team.from_name("Sweden")        # 13 Sweden   E  7500  5.49 TJ      +2 QUALIFIED
    SwLand = Team.from_name("SwLand")        # 12 SwLand   A  7000  4.09 BARDIA  +0 QUALIFIED
    Turkey = Team.from_name("Turkey")        # 11 Turkey   A  5000  5.39 COOPER  +0
    Ukraine = Team.from_name("Ukraine")      # 17 Ukraine  C 10000  5.12 TJ      +4 QUALIFIED
    Wales = Team.from_name("Wales")          # 15 Wales    A 10000  2.91 RYAN    +0 QUALIFIED

    all_games = [
        Game(Turkey,   Italy,    0, Italy,    0, 3), # [ 0] Cooper vs Ryan   Italy    -1.5  Fri 6/11 || Ryan +3
        Game(Wales,    SwLand,   0, None,     1, 1), # [ 1] Ryan   vs Bardia Swland   - .25 Sat 6/12 || Ryan +1 Bardia +1
        Game(Denmark,  Finland,  0, Finland,  0, 1), # [ 2] Cooper vs Andrew Denmark  -1.25 Sat 6/12 || Andrew +3
        Game(Belgium,  Russia,   0, Belgium,  3, 0), # [ 3] Cooper vs Micah  Belgium  - .25 Sat 6/12 || Cooper +3
        Game(England,  Croatia,  0, England,  1, 0), # [ 4] TJ     vs Micah  England  - .75 Sun 6/13 || TJ +3
        Game(Austria,  NorthMac, 0, Austria,  3, 1), # [ 5] Andrew vs Micah  Austria  - .75 Sun 6/13 || Andrew +3
        Game(NLands,   Ukraine,  0, NLands,   3, 2), # [ 6] Ryan   vs TJ     NLands   - .75 Sun 6/13 || Ryan +3
        Game(Scotland, CzecRep,  0, CzecRep,  0, 2), # [ 7] Bardia vs Ryan   -------- ----- Mon 6/14 || Ryan +3
        Game(Poland,   Slovakia, 0, Slovakia, 1, 2), # [ 8] Andrew vs TJ     Poland   - .5  Mon 6/14 || TJ +3
        Game(Spain,    Sweden,   0, None,     0, 0), # [ 9] Micah  vs TJ     Spain    -1.25 Mon 6/14 || Micah +1 TJ +1
        Game(Hungary,  Portugal, 0, Portugal, 0, 3), # [10] Cooper vs Bardia Portugal -1    Tue 6/15 || Bardia +3
        Game(France,   Germany,  0, France,   1, 0), # [11] Andrew vs Bardia -------- ----- Tue 6/15 || Andrew +3
        Game(Finland,  Russia,   0, Russia,   0, 1), # [12] Andrew vs Micah  Russia   - .75 Wed 6/16 || Micah +3
        Game(Turkey,   Wales,    0, Wales,    0, 2), # [13] Cooper vs Ryan   Turkey   - .25 Wed 6/16 || Ryan +3
        Game(Italy,    SwLand,   0, Italy,    3, 0), # [14] Ryan   vs Bardia Italy    - .75 Wed 6/16 || Ryan +3
        Game(Ukraine,  NorthMac, 0, Ukraine,  2, 1), # [15] TJ     vs Micah  Ukraine  - .75 Thu 6/17 || TJ +3
        Game(Denmark,  Belgium,  0, Belgium,  1, 2), # [16] Cooper vs Cooper Belgium  -1.5  Thu 6/17 || Cooper +3
        Game(NLands,   Austria,  0, NLands,   2, 0), # [17] Ryan   vs Andrew NLands   -1    Thu 6/17 || Ryan +3
        Game(Sweden,   Slovakia, 0, Sweden,   1, 0), # [18] TJ     vs TJ     Sweden   - .5  Fri 6/18 || TJ +3
        Game(Croatia,  CzecRep,  0, None,     1, 1), # [19] Micah  vs Ryan   Croatia  - .25 Fri 6/18 || Micah +1 Ryan +1
        Game(England,  Scotland, 0, None,     0, 0), # [20] TJ     vs Bardia England  -1.25 Fri 6/18 || TJ +1 Bardia +1
        Game(Hungary,  France,   0, None,     1, 1), # [21] Cooper vs Andrew France   -1.25 Sat 6/19 || Cooper +1 Andrew +1
        Game(Portugal, Germany,  0, Germany,  2, 4), # [22] Bardia vs Bardia Germany  - .25 Sat 6/19 || Bardia +3
        Game(Spain,    Poland,   0, None,     1, 1), # [23] Micah  vs Andrew Spain    -1    Sat 6/19 || Micah +1 Andrew +1
        Game(Italy,    Wales,    0, Italy,    1, 0), # [24] Ryan   vs Ryan   Italy    -1    Sun 6/20 || Ryan +3
        Game(SwLand,   Turkey,   0, SwLand,   3, 1), # [25] Bardia vs Cooper SwLand   - .25 Sun 6/20 || Bardia +3
        Game(NorthMac, NLands,   0, NLands,   0, 3), # [26] Micah  vs Ryan   NLands   -1.75 Mon 6/21 || Ryan +3
        Game(Ukraine,  Austria,  0, Austria,  0, 1), # [27] TJ     vs Andrew -------- ----- Mon 6/21 || Andrew +3
        Game(Russia,   Denmark,  0, Denmark,  1, 4), # [28] Micah  vs Cooper Denmark  - .5  Mon 6/21 || Cooper +3
        Game(Finland,  Belgium,  0, Belgium,  0, 2), # [29] Andrew vs Cooper Belgium  -1.75 Mon 6/21 || Cooper +3
        Game(CzecRep,  England,  0, England,  0, 1), # [30] Ryan   vs TJ     England  -1    Tue 6/22 || TJ +3
        Game(Croatia,  Scotland, 0, Croatia,  3, 1), # [31] Micah  vs Bardia Croatia  - .5  Tue 6/22 || Micah +3
        Game(Slovakia, Spain,    0, Spain,    0, 5), # [32] TJ     vs Micah  Spain    -1.75 Wed 6/23 || Micah +3
        Game(Sweden,   Poland,   0, Sweden,   3, 2), # [33] TJ     vs Andrew -------- ----- Wed 6/23 || TJ +3
        Game(Germany,  Hungary,  0, None,     2, 2), # [34] Bardia vs Cooper Germany  -1.5  Wed 6/23 || Bardia +1 Cooper +1
        Game(Portugal, France,   0, None,     2, 2), # [35] Bardia vs Andrew -------- ----- Wed 6/23 || Bardia +1 Andrew +1
        Game(Italy,   Austria,   1, Italy,    2, 1), # [36] Ryan   vs Andrew Sat 6/26 || Ryan +3
        Game(Denmark, Wales,     1, Denmark,  4, 0), # [37] Cooper vs Ryan   Sat 6/26 || Cooper +3
        Game(Belgium, Portugal,  1, Belgium,  1, 0), # [38] Cooper vs Bardia Sun 6/27 || Cooper +3
        Game(NLands,  CzecRep,   1, CzecRep,  0, 2), # [39] Ryan   vs Ryan   Sun 6/27 || Ryan +3
        Game(France,  SwLand,    1, SwLand,   3, 3), # [40] Andrew vs Bardia Mon 6/28 || Bardia +3
        Game(Spain,   Croatia,   1, Spain,    5, 3), # [41] Micah  vs Micah  Mon 6/28 || Micah +3
        Game(Sweden,  Ukraine,   1, Ukraine,  1, 2), # [42] TJ     vs TJ     Tue 6/28 || TJ +3
        Game(England, Germany,   1, England,  2, 0), # [43] TJ     vs Bardia Tue 6/28 || TJ +3
        Game(SwLand,  Spain,     2, Spain,    1, 1), # [44] Bardia vs Micah  Fri 7/2  || Micah +3
        Game(Belgium, Italy,     2, Italy,    1, 2), # [45] Cooper vs Ryan   Fri 7/2  || Ryan +3
        # Game(CzecRep, Denmark,   2), #47# [46] Ryan vs Cooper  Sat 7/3
        # Game(Ukraine, England,   2), #48# [47] TJ vs TJ        Sat 7/3
    ]

    # if modifier is not None and modifier[0] >= 44 and modifier[0] <= 47:
        # all_games[modifier[0]] = modifier[1]

    #Semi-finals
    # all_games.append(Game(all_games[45].winner, all_games[44].winner, 3)) #49# [48]
    # all_games.append(Game(all_games[47].winner, all_games[46].winner, 3)) #50# [49]

    # if modifier is not None and modifier[0] >= 48 and modifier[0] <= 49:
        # all_games[modifier[0]] = modifier[1]

    #Final
    # all_games.append(Game(all_games[48].winner, all_games[49].winner, 4)) # Match 51

    return all_games

def simulate_tournament():
    all_games = []
    teams = Team.all_teams()
    records = {}
    elim = {"A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "G": [], "H": []}
    elim_records = {"A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "G": [], "H": []}

    for team in teams:
        records[team.name] = Record(team)

    for group in ["A", "B", "C", "D", "E", "F", "G", "H"]:
        all_games += simulate_group(group)

    for game in all_games:
        for team in game.teams:
            records[team.name].add(game)

    for record in records.values():
        group = record.team.group
        elim_records[group].append(record)

    for group in ["A", "B", "C", "D", "E", "F", "G", "H"]:
        elim_records[group] = sorted(elim_records[group])
        for record in elim_records[group]:
            elim[group].append(record.team)

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

    return all_games

def multi_draft_sim():
    player_ranks = [[],[],[],[],[],[]]

    draft_runs = 1
    for i in range(draft_runs):
        print("Draft Simulation: %.2f%%" % (i/draft_runs*100), end='\r')
        drafts = [
            Draft(0),
            Draft(1),
            Draft(2),
            Draft(3),
            Draft(4),
            Draft(5)
        ]

        simulate_draft(drafts, sorted_teams)
        for draft in drafts:
            draft.add_records(super_records.values())

        sorted_drafts = sorted(drafts)
        for i, draft in enumerate(sorted_drafts):
            player_ranks[draft.player].append(i)
            #print(draft)

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

    final_records = {"A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "X": []}

    for record in sorted_records:
        group = record.team.group
        final_records[group].append(record.team)

    print("Results: ")
    for group in ["A", "B", "C", "D", "E", "F"]:
        print("  Group %s: " % (group))
        for team in final_records[group]:
            print(records[team.name])


def main_sim(runs, modifier, t1, t2):
    teams = Team.all_teams()
    super_records = {}
    for team in teams:
        super_records[team.name] = SuperRecord(team)

    winners = {"ANDREW":0, "BARDIA":0, "COOPER":0, "MICAH":0, "RYAN":0, "TJ":0}
    for i in range(runs):
        print("Tournament Simulation: %.2f%%" % (i/runs*100), end='\r')
        #all_games = real_tournament(modifier)
        all_games = simulate_tournament()

        records = {}
        for team in teams:
            records[team.name] = Record(team)

        for game in all_games:
            for team in game.teams:
                records[team.name].add(game)

        for team in teams:
            super_records[team.name].collect(records[team.name])

        drafts = true_draft()

        for draft in drafts:
            draft.add_records(records.values())

        # for draft in sorted(drafts):
        #     print(draft)

        sorted_drafts = sorted(drafts)
        if sorted_drafts[0].score(0) == sorted_drafts[1].score(0) and sorted_drafts[0].goal_differential == sorted_drafts[1].goal_differential and sorted_drafts[0].score(0) == sorted_drafts[2].score(0) and sorted_drafts[0].goal_differential == sorted_drafts[2].goal_differential:
            winners[sorted_drafts[0].player] += 0.3333333
            winners[sorted_drafts[1].player] += 0.3333333
            winners[sorted_drafts[2].player] += 0.3333333
        elif sorted_drafts[0].score(0) == sorted_drafts[1].score(0) and sorted_drafts[0].goal_differential == sorted_drafts[1].goal_differential:
            winners[sorted_drafts[0].player] += 0.5
            winners[sorted_drafts[1].player] += 0.5
        else:
            winners[sorted_drafts[0].player] += 1

    sorted_winners = dict(sorted(winners.items(), key=lambda item: -item[1]))

    print("==============================")
    if modifier is not None:
        if modifier[1].winner is None:
            print("Tie\n==============================")
        else:
            print("%s\n==============================" % (modifier[1].winner.name))
    else:
        print("Baseline\n==============================")

    for item in sorted_winners.items():
        print("%6s: %.6f%%" % (item[0], item[1] / runs * 100))

    print("")
    print("%10s %s %5.2f" % (t1.name, t1.group, super_records[t1.name].points(0)["mean"]))
    print("%10s %s %5.2f" % (t2.name, t2.group, super_records[t2.name].points(0)["mean"]))

    if modifier is None:
        sorted_sd = {k: v for k, v in sorted(super_records.items(), key=lambda item: -item[1].points(0)["mean"])}
        for team in sorted_sd.values():
            print(team)


    drafts = true_draft()
    for draft in drafts:
        print("\n%s:" % (draft.player))
        total = 0
        gd = 0
        for team in draft.teams:
            print("  %10s %s %5.2f %d" % (team.name, team.group, super_records[team.name].points(0)["mean"], super_records[team.name].goal_differential), )
            total += super_records[team.name].points(0)["mean"]
            gd += super_records[team.name].goal_differential

        print("       Total   %5.2f %d" % (total, gd))


def combo_sim(count, game_number, t1, t2):
    main_sim(count, None, t1, t2)
    # main_sim(count, (game_number, Game(t1,    t2,   1, t1, 1, 0)), t1, t2)
    # main_sim(count, (game_number, Game(t1,    t2,   1, t2, 0, 1)), t1, t2)
    #main_sim(count, (game_number, Game(t1,    t2,   0, None, 1, 1)), t1, t2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', '--debug', action='store_true')
    args = parser.parse_args()

    if args.debug:
        print("Debug")

    ARGENTINA = Team.from_name("ARGENTINA")
    AUSTRLIA = Team.from_name("AUSTRLIA")
    BELGIUM = Team.from_name("BELGIUM")
    BRAZIL = Team.from_name("BRAZIL")
    CAMEROON = Team.from_name("CAMEROON")
    CANADA = Team.from_name("CANADA")
    COSTARICA = Team.from_name("COSTA RICA")
    CROATIA = Team.from_name("CROATIA")
    DENMARK = Team.from_name("DENMARK")
    ECUADOR = Team.from_name("ECUADOR")
    ENGLAND = Team.from_name("ENGLAND")
    FRANCE = Team.from_name("FRANCE")
    GERMANY = Team.from_name("GERMANY")
    GHANA = Team.from_name("GHANA")
    IRAN = Team.from_name("IRAN")
    JAPAN = Team.from_name("JAPAN")
    KOREA = Team.from_name("KOREA")
    MEXICO = Team.from_name("MEXICO")
    MOROCCO = Team.from_name("MOROCCO")
    NETHERLANDS = Team.from_name("NETHERLANDS")
    POLAND = Team.from_name("POLAND")
    PORTUGAL = Team.from_name("PORTUGAL")
    QATAR = Team.from_name("QATAR")
    SAUDIARABIA = Team.from_name("SAUDI ARABIA")
    SENEGAL = Team.from_name("SENEGAL")
    SERBIA = Team.from_name("SERBIA")
    SPAIN = Team.from_name("SPAIN")
    SWITZERLAND = Team.from_name("SWITZERLAND")
    TUNISIA = Team.from_name("TUNISIA")
    URUGUAY = Team.from_name("URUGUAY")
    USA = Team.from_name("USA")
    WALES = Team.from_name("WALES")

    #combo_sim(50, 46, CzecRep, Denmark)
    #main_sim(50000, None, t1, t2)
    #main_sim(1, None, CzecRep, England)
    main_sim(10000, None, QATAR, ECUADOR)

    # sorted_records = sorted(list(super_records.values()))

    # for record in sorted_records:
    #     print(record)

    # sorted_teams = sorted(teams)
    # for index, team in enumerate(sorted_teams):
    #     print("%2d %s [%5.2f]" % (index+1, team, super_records[team.name].points(0)["mean"]))

