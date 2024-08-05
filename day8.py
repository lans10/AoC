"""
Day 8 of Advent of Code 2023
"""
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
    print(moves)
    print(nodes)
    solve_part1(moves, nodes)

def solve_part1(moves, nodes):
    """
    Solves part 1 by running a loop starting with node AAA until current
    node is ZZZ. Follows instructions from variable moves onto nodes.
    moves: String of moves (L for left, R for right. E.g. "LRLRLR")
    nodes: Dictionary of nodes ({'AAA':('BBB','CCC')})
    """
    count = 0
    curr = 'AAA'
    while curr != 'ZZZ':
        for c in moves:
            if c == "L":
                curr = nodes[curr][0]
            else:
                curr = nodes[curr][1]
            count += 1
    print(count)
if __name__ == '__main__':
    main()
