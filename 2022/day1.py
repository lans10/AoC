"""
Day 1 of Advent of Code 2022
"""
def main():
    with open("input", "r", encoding="utf-8") as f:
            inp = f.readlines()
    currentSum=0
    calories=[]
    for line in inp:
        if line!="\n":
            currentSum+=int(line)
        else:
            calories.append(currentSum)
            currentSum=0
    sortedCals = sorted(calories)
    print("Highest calories: "+ str(sortedCals[-1]))
    print("Top 3 calories:   "+ str(sortedCals[-1]+sortedCals[-2]+sortedCals[-3]))

if __name__ == '__main__':
    main()
