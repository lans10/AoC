"""
Day 6 of Advent of Code 2023
"""
import math
from numpy import prod

with open("input", "r", encoding="utf-8") as f:
    inp = f.readlines()

def record(time, distance):
    """
    Record time for one race
    """
    curr_score = 0
    beat = {}
    curr_time = 1
    while curr_time<=time:
        curr_score+=(time-curr_time)*curr_time
        if curr_score>distance:
            beat[curr_time]=curr_score
        curr_score=0
        curr_time+=1
    return len(beat)

def main():
    """
    Part 1 has all scores
    Part 2 is one big race
    """
    #part one
    times = (''.join(inp[0].split(":")[-1]).split())
    times = [int(s) for s in times]
    distances = (''.join(inp[1].split(":")[-1]).split())
    distances = [int(s) for s in distances]
    scores = []
    for i, time in enumerate(times):
        scores.append(record(time, distances[i]))
    print(prod(scores))

    #part two
    times = int(''.join([str(x) for x in times]))
    distances = int(''.join([str(x) for x in distances]))

    print(inversemiddleout(times,distances,50000))

    print(literalmath(times,distances))

def inversemiddleout(time, distance, inc=1):
    """
    I did try going middle and outward...thanks silicon valley
    """
    losses=0
    l_time,r_time=1,time
    l_loss,r_loss=True,True
    while l_loss or r_loss:
        if not beat_helper(l_time,time,distance):
            losses+=inc
        else:
            l_loss=False
            if inc!=1:
                for i in range(l_time-inc,l_time):
                    if beat_helper(i,time,distance):
                        losses-=1
        if not beat_helper(r_time,time,distance):
            losses+=inc
        else:
            r_loss=False
            if inc!=1:
                for i in range(r_time+1,r_time+inc):
                    if beat_helper(i,time,distance):
                        losses-=1
        l_time+=inc
        r_time-=inc
    return time-losses

def beat_helper(curr_time, time, distance):
    """
    I realize this is a quadratic equation
    """
    return ((time-curr_time)*curr_time)>distance
#beat_helper() staring me in the face
def literalmath(time,distance):
    """
    Solutions to a quadratic equation
    """
    a,b,c = -1,time,-1*distance
    x1 = math.ceil(-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
    x2 = math.floor(-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
    return int(x2-x1-1)
main()
