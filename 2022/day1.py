"""
Day 1 of Advent of Code 2022
"""
def main():
"""
Uses white space as a separator
"""
    with open("input", "r", encoding="utf-8") as f:
        inp = f.readlines()
    current_sum=0
    calories=[]
    for line in inp:
        if line!="\n":
            current_sum+=int(line)
        else:
            calories.append(current_sum)
            current_sum=0
    sorted_cals = sorted(calories)
    print("Highest calories: "+ str(sorted_cals[-1]))
    print("Top 3 calories:   "+ str(sorted_cals[-1]+sorted_cals[-2]+sorted_cals[-3]))

if __name__ == '__main__':
    main()
