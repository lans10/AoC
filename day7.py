from functools import cmp_to_key

with open("input", "r") as f:
    inp = f.readlines()

type={"high":0,"one":1, "two":2, "three":3, "full":4, "four":5, "five":6}
card_p1={"A":12, "K":11, "Q":10, "J":9, "T":8, "9":7, "8":6, "7":5, "6":4, "5":3, "4":2, "3":1, "2":0}
card_p2={"A":12, "K":11, "Q":10, "T":8, "9":7, "8":6, "7":5, "6":4, "5":3, "4":2, "3":1, "2":0, "J":-1}

def cmp(a,b):
    if a>b:
        return 1
    elif b>a:
        return -1
    return 0
    
def compareCard(card1, card2, part=2):
    if part==1:
        return cmp(card_p1[card1],card_p1[card2])
    return cmp(card_p2[card1],card_p2[card2])

#same type different strength
def compareHandPart1(hand1, hand2):
    for i in range(len(hand1)):
        if hand1[i]!=hand2[i]:
            return compareCard(hand1[i],hand2[i],1)
    return 0
    
def compareHandPart2(hand1, hand2):
    for i in range(len(hand1)):
        if hand1[i]!=hand2[i]:
            return compareCard(hand1[i],hand2[i])
    return 0

def parseHand(hand,part=2):
    #I am ashamed of what you may find here.
    curr_hand = {}
    for c in sorted(set(hand)):
        c_count = hand.count(c)
        curr_hand[c]=c_count
    l1 = list(curr_hand.values())
    l1.sort()
    if 5 in l1:
        score =  6
    elif 4 in l1:
        score =   5
    elif 3 in l1 and 2 in l1:
        score =   4
    elif 3 in l1 and 1 in l1:
        score =   3
    elif l1==[1,2,2]:
        score =   2 
    elif l1==[1,1,1,1,1]:
        score =   0 
    else:
        score =   1
    if part==2:
        if "J" in hand:
            if curr_hand["J"]==1:
                if score==1:
                    score=3
                elif score==2:
                    score=4
                elif score ==3:
                    score=5
                else:
                    score+=1
            elif curr_hand["J"]==2:
                if score==2:
                    score=5
                else:
                    score+=2
            elif curr_hand["J"]==3:
                score+=2
            elif curr_hand["J"]==4:
                score+=1
            if score>6:
                score=6
    return score 
def main():
    solve(1)
    solve(2)
    
def solve(part=2):
    hand_bid = {}
    #HAND: [bid]
    
    ordered_hands = [[] for i in range(len(type))]
    # [[hands that are high], [hands that are one pair], ..., [hands that are five of a kind]]
    # rank internally by card strength L->R
    # rank is trueindex+1
    for hand in inp:
        hand = hand.split()
        hand_bid[hand[0]]=int(hand[1])
        
    for hand in hand_bid:
        ordered_hands[parseHand(hand,part)].append(hand)
    for i in range(len(ordered_hands)):
        if len(ordered_hands[i])>1:
            if part==1:
                ordered_hands[i]=sorted(ordered_hands[i], key=cmp_to_key(compareHandPart1))
            else:
                ordered_hands[i]=sorted(ordered_hands[i], key=cmp_to_key(compareHandPart2))

    rank = 1
    winnings = 0
    for row in ordered_hands:
        for hand in row:
            winnings+=hand_bid[hand]*rank
            rank+=1
    
    print(winnings)
main()
