"""
Day 6 of Advent of Code 2022
"""
from collections import deque
from copy import deepcopy as copy
def main():
    """
    marker
    """
    with open("sample", "r", encoding="utf-8") as f:
        inp = f.read()
    read = ''
    for i in range(0,len(inp)):
        if len(read)>=4:
            if inp[i] in read:
                check = read[len(read)-3:]+inp[i]
                print(check)
                if len(set(check))==len(check):
                    print(i-1)
                    break
        read+=inp[i]
if __name__ == '__main__':
    main()
