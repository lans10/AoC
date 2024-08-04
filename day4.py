with open("input.txt", "r", encoding="utf-8") as f:
    inp = f.readlines()
d = {}
def main():
    points=0
    for card in inp:
        card = card.split(':')
        num = ''.join(card[0]).split()[1]
        card = ''.join(card[1])
        card = card.split('|')
        win = ''.join(card[0]).split()
        elf = ''.join(card[1]).split()
        match = 0
        for n in win:
            if n in elf:
                match+=1
        if match>0:
            points+=2**(match-1)
        d[num]=[match,1]
    print(points)  
    sc = 0
    for key in d.keys():
        #print("Card "+key+": "+str(d[key]))
        for k in range(d[key][1]):
            for i in range(1, d[key][0]+1):
                d[str(int(key)+i)][1]+=1
        sc+=d[key][1]
    print(sc)

main()
