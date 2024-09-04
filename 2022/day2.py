"""
Day 2 of Advent of Code 2022
"""
from copy import deepcopy as copy
def main():
    """
    RPS
    """
    with open("input", "r", encoding="utf-8") as f:
        inp = f.readlines()
    rule = {}
    hand = [None]*7
    rps = ['',"X","Y","Z"]
    rule = {"A":copy(hand),"B":copy(hand),"C":copy(hand)}
    # X rock Y paper Z scissors
    # A rock
    rule["A"][0]="Z"
    rule["A"][3]="X"
    rule["A"][6]="Y"
    # B paper
    rule["B"][0]="X"
    rule["B"][3]="Y"
    rule["B"][6]="Z"
    # C scissors
    rule["C"][0]="Y"
    rule["C"][3]="Z"
    rule["C"][6]="X"
    
    points = 0
    for line in inp:
        line = line.split()
        point = rule[line[0]].index(line[1]) + rps.index(line[1])
        points += point
    print("Part 1: "+str(points))
    
    points = 0
    new_rules = {"X":0,"Y":3,"Z":6}
    for line in inp:
        line = line.split()
        point = new_rules[line[1]]
        #Find what hand to play and assign point accordingly
        point += rps.index(rule[line[0]][new_rules[line[1]]])
        points+=point
    print("Part 2: "+str(points))
        
if __name__ == '__main__':
    main()
