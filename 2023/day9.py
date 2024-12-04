"""
Day 9 of Advent of Code 2023
"""
def main():
    """
    Part 1 solves for predicting next and previous number in a sequence
    """
    filename = "input"
    with open(filename, "r", encoding="utf-8") as f:
        inp = f.readlines()
    print(solve_part1(inp))
    print(solve_part2(inp))

def solve_part1(inp):
    """
    Solves part 1. Predict next number in sequence
    """
    pred = []
    rows = []
    for row in inp:
        rows.append([[eval(i) for i in row.split()]])
    for row in rows:
        while row[-1] != [0] * len(row[-1]):
            l1 = []
            for i, _ in enumerate(row[-1]):
                if i+1<len(row[-1]):
                    l1.append(row[-1][i+1]-row[-1][i])
            row.append(l1)
    for row in rows:
        for i, _ in reversed(list(enumerate(row))):
            if i==len(row)-1:
                row[i].append(0)
            else:
                row[i].append(row[i][-1]+row[i+1][-1])
        pred.append(row[0][-1])
    return sum(pred)

def solve_part2(inp):
    """
    Solves part 2. Predicting value before first value
    """
    pred = []
    rows = []
    for row in inp:
        rows.append([[eval(i) for i in row.split()]])
    for row in rows:
        while row[-1] != [0] * len(row[-1]):
            l1 = []
            for i, _ in enumerate(row[-1]):
                if i+1<len(row[-1]):
                    l1.append(row[-1][i+1]-row[-1][i])
            row.append(l1)
    for row in rows:
        for i, _ in reversed(list(enumerate(row))):
            if i==len(row)-1:
                row[i].append(0)
            else:
                row[i].insert(0,row[i][0]-row[i+1][0])
        pred.append(row[0][0])
    return sum(pred)

if __name__ == '__main__':
    main()
