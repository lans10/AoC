"""
Day 8 of Advent of Code 2023
"""
import numpy as np
def main():
    """
    Part 1 solves for number of moves to move from AAA to ZZZ
    """
    filename = "input"
    with open(filename, "r", encoding="utf-8") as f:
        inp = f.readlines()
        moves =inp.pop(0).split()[0]
    nodes = {}
    for line in inp:
        if line != "\n":
            line = line.split("=")
            key = line[0].split()[0]
            line = line[1].split()
            value = (line[0][1:4], line[1][:3])
            nodes[key]=value
    solve_part1(moves, nodes)
    solve_part2(moves, nodes)

def solve_part1(moves, nodes):
    """
    Solves part 1 by running a loop starting with node AAA until current
    node is ZZZ. Follows instructions from variable moves onto nodes.
    moves: String of moves (L for left, R for right. E.g. "LRLRLR")
    nodes: Dictionary of nodes ({'AAA':('BBB','CCC')})
    """
    count = 0
    curr = 'AAA'
    if 'AAA' in nodes:
        while curr != 'ZZZ':
            for c in moves:
                if c == "L":
                    curr = nodes[curr][0]
                else:
                    curr = nodes[curr][1]
                count += 1
        print(count)

def solve_part2(moves, nodes):
    """
    Solves part 2 by running a loop starting with every node that ends with A,
    until they end with Z. Follows instructions from variable moves onto nodes.
    moves: String of moves (L for left, R for right. E.g. "LRLRLR")
    nodes: Dictionary of nodes ({'AAA':('BBB','CCC')})
    """
    count = 0
    targets = []
    for key, _ in nodes.items():
        if key[-1] == 'A':
            curr = key
            while curr[-1] != 'Z':
                for c in moves:
                    if c == "L":
                        curr = nodes[curr][0]
                    else:
                        curr = nodes[curr][1]
                    count += 1
            if count not in targets:
                targets.append(count)
            count = 0
            print(targets)
    print(np.lcm.reduce(targets))

if __name__ == '__main__':
    main()
