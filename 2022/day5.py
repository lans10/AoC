"""
Day 5 of Advent of Code 2022
"""
from collections import deque
from copy import deepcopy as copy
def main():
    """
    stacks
    """
    with open("input", "r", encoding="utf-8") as f:
        inp = f.readlines()
    num, src, dest = 0, 0, 0
    stacks= []
    size = None
    i=0
    while "1   2" not in inp[i]:
        line = inp[i]
        line = [i for i in inp[i] if i!='\n']
        line = [line[i] for i in range(1, len(line), 4)]
        if size==None:
            stacks=[deque() for i in range(len(line)+1)]
            size = len(line)
        for j in range(0,len(line)):
            if line[j]!=' ':
                stacks[j+1].append(line[j])
        i+=1
    i+=2
    moves = i
    stacks_two = copy(stacks)
    while i<len(inp):
        line = inp[i].split()
        num, src, dest = int(line[1]), int(line[3]), int(line[5])
        for j in range(num):
            c = stacks[src].popleft()
            stacks[dest].appendleft(c)
        i+=1
    msg = ""
    for stack in stacks:
        if len(stack)>0:
            msg+=stack[0]
    print("Part 1: "+msg)
    i = moves
    stacks = stacks_two
    while i<len(inp):
        line = inp[i].split()
        num, src, dest = int(line[1]), int(line[3]), int(line[5])
        temp = deque()
        for j in range(num):
            c = temp.appendleft(stacks[src].popleft())
        while len(temp)>0:
            stacks[dest].appendleft(temp.popleft())
        i+=1
    msg = ""
    for stack in stacks:
        if len(stack)>0:
            msg+=stack[0]
    print("Part 2: "+msg)
if __name__ == '__main__':
    main()
