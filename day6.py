from numpy import prod
import math

with open("input", "r") as f:
    inp = f.readlines()

def record(time, distance):
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
    #part one
    times = (''.join(inp[0].split(":")[-1]).split())
    times = [int(s) for s in times]
    distances = (''.join(inp[1].split(":")[-1]).split())
    distances = [int(s) for s in distances]
    scores = []
    for i in range(len(times)):
        scores.append(record(times[i], distances[i]))
    print(prod(scores))
    
    #part two
    times = int(''.join([str(x) for x in times]))
    distances = int(''.join([str(x) for x in distances]))
    
    print(inversemiddleout(times,distances,50000))
    
    print(literalmath(times,distances))
    
def inversemiddleout(time, distance, inc=1):
    #I did try going middle and outward...thanks silicon valley
    losses=0
    lTime,rTime=1,time
    lLoss,rLoss=True,True
    while lLoss or rLoss:
        if not beat_helper(lTime,time,distance):
            losses+=inc 
        else:
            lLoss=False
            if inc!=1:
                for i in range(lTime-inc,lTime):
                    if beat_helper(i,time,distance):
                        losses-=1
        if not beat_helper(rTime,time,distance):
            losses+=inc 
        else:
            rLoss=False
            if inc!=1:
                for i in range(rTime+1,rTime+inc):
                    if beat_helper(i,time,distance):
                        losses-=1
        lTime+=inc
        rTime-=inc
    return time-losses

def beat_helper(curr_time, time, distance):
    return ((time-curr_time)*curr_time)>distance
#beat_helper() staring me in the face
def literalmath(time,distance):
    a,b,c = -1,time,-1*distance
    x1 = math.ceil(-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
    x2 = math.floor(-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
    return int(x2-x1-1)
main()
