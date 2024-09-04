"""
Day 3 of Advent of Code 2022
"""
def main():
    """
    rucksack
    """
    with open("input", "r", encoding="utf-8") as f:
        inp = f.readlines()
    left, right = [], []
    total = 0
    for line in inp:
        left,right =list(line[:len(line)//2]), list(line[len(line)//2:].strip())
        common = ord(list(set(left) & set(right))[0])
        if common>96:
            common-=96
        else:
            common-=38
        total += common
    print("Part 1: "+str(total))
    total = 0
    for i in range(0,len(inp),3):
        a,b,c = list(inp[i].strip()),list(inp[i+1].strip()),list(inp[i+2].strip())
        common = ord(list(set(a) & set(b) & set(c))[0])
        if common>96:
            common-=96
        else:
            common-=38
        total += common
    print("Part 2: "+str(total))

if __name__ == '__main__':
    main()
