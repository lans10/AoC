"""
Day 6 of Advent of Code 2022
"""
def main():
    """
    marker
    """
    with open("input", "r", encoding="utf-8") as f:
        inp = f.read()
    read_text = ''
    for i,v in enumerate(inp):
        if len(read_text)>=4:
            check = read_text[len(read_text)-3:]+v
            if len(set(check))==len(check):
                print("Part 1:"+str(i+1))
                break
        read_text+=v
if __name__ == '__main__':
    main()
