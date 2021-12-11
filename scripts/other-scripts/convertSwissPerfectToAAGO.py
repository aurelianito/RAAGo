#!/usr/bin/python3

"""
Convert SwissPerfect .txt results to .aago file

Known limitations:
 * Uses a single date (passed via command line) because the .txt does not have dates
 * All wins are attributed to white because the .txt file has no color information
 * All games are assumed to be even games because the .txt file has no handicap information
"""

import sys
import argparse
import re

def parse_args(argv):
    parser = argparse.ArgumentParser(description="Convert SwissPerfect .txt results to .aago file")
    parser.add_argument("-n", "--name", help="Tournament name (default=%(default)s)", default="SwissPerfect Tournament")
    parser.add_argument("-d", "--date", help="Tournament date")
    parser.add_argument("txt_file", help=".txt file generated by SwissPerfect")
    return parser.parse_args(args=argv[1:])

def main(argv):
    args = parse_args(argv)

    with open(args.txt_file, "r", encoding='cp1252') as f:
        lines = f.read().split("\n")

    header = lines[0].split('|')

    assert(header[0] == 'Nº')
    assert(header[1] == 'Nombre')
    assert(header[2] == 'Feder')
    assert(header[3] == 'Total')

    round_count = header[-1]

    print("[Options]")
    print(f"Name={args.name}")
    print(f"StartDate={args.date}") #all dates are the same date
    print(f"EndDate={args.date}") #all dates are the same date
    print(f"Rounds={round_count}")

    rounds = []
    for _ in range(int(round_count)): 
        rounds.append(set())
    players = []
    win_regex = re.compile("^(\d+):W$")

    for i, l in enumerate(lines[2:]):
        if l:
            player_id = str(i+1)
            l = l.split('|')
            players.append((l[1], l[2]))

            for j, game in enumerate(l[4:]):
                m = win_regex.match(game)
                if m:
                    rounds[j].add((player_id, m.groups()[0]))

    print(f"Numberofplayers={len(players)}")
    for i, data in enumerate(players):
        print(f"[Player{i+1}]")
        print(f"Name={data[0]}")
        print(f"Category={data[1]}")

    for i, round in enumerate(rounds):
        print(f"[Round{i}]")
        print(f"Date={args.date}")
        for j, (winner, loser) in enumerate(round):
            print(f"Game{j}Player1={winner}")
            print(f"Game{j}Player2={loser}")
            print(f"Game{j}Handicap=0")
            print(f"Game{j}Result=W")

if __name__ == "__main__":
    main(sys.argv)
