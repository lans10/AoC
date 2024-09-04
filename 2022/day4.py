"""
Day 4 of Advent of Code 2022
"""
def main():
    """
    pairs
    """
    with open("input", "r", encoding="utf-8") as f:
        inp = f.readlines()
    within_count, overlap_count = 0, 0
    for line in inp:
        left,right = line.strip().split(',')
        left = left.split('-')
        right = right.split('-')
        for i in range(2):
            left[i]=int(left[i])
            right[i]=int(right[i])
        if within(left,right):
            within_count+=1
        if overlap(left,right):
            overlap_count+=1
    print("Part 1: "+str(within_count))
    print("Part 2: "+str(overlap_count))

def within(a,b):
    #assuming a,b is list of 2 int
    if b[-1]-b[0]<a[-1]-a[0]:
        a,b = b,a
    if a[0]>=b[0] and a[-1]<=b[-1]:
        return True
    return False
def overlap(a,b):
    #assuming a,b is list of 2 int
    return a[-1] >= b[0] and b[-1] >= a[0]
if __name__ == '__main__':
    main()
