from functools import cmp_to_key

with open("input", "r") as f:
    inp = f.readlines()

type={"high":0,"one":1, "two":2, "three":3, "full":4, "four":5, "five":6}
card={"A":12, "K":11, "Q":10, "J":9, "T":8, "9":7, "8":6, "7":5, "6":4, "5":3, "4":2, "3":1, "2":0}

hand_bid = {}
#HAND: [bid]

ordered_hands = [[] for i in range(len(type))]
# [[hands that are high], [hands that are one pair], ..., [hands that are five of a kind]]
# rank internally by card strength L->R
# rank is trueindex+1

def cmp(a,b):
    if a>b:
        return 1
    elif b>a:
        return -1
    return 0
    
def compareCard(card1, card2):
    return cmp(card[card1],card[card2])

#same type different strength
def compareHand(hand1, hand2):
    for i in range(len(hand1)):
        if hand1[i]!=hand2[i]:
            return compareCard(hand1[i],hand2[i])
    return 0

def parseHand(hand):
    curr_hand = {}
    for c in sorted(set(hand)):
        c_count = hand.count(c)
        #print(c+" appeared "+str(c_count)+" times")
        curr_hand[c]=c_count
    l1 = list(curr_hand.values())
    l1.sort()
    if 5 in l1:
        return 6
    elif 4 in l1:
        return 5
    elif 3 in l1 and 2 in l1:
        return 4
    elif 3 in l1 and 1 in l1:
        return 3
    elif l1==[1,2,2]:
        return 2 
    elif l1==[1,1,1,1,1]:
        return 0 
    return 1
def main():
    for hand in inp:
        hand = hand.split()
        hand_bid[hand[0]]=int(hand[1])
    for hand in hand_bid:
        ordered_hands[parseHand(hand)].append(hand)
    for i in range(len(ordered_hands)):
        if len(ordered_hands[i])>1:
            ordered_hands[i]=sorted(ordered_hands[i], key=cmp_to_key(compareHand))
    rank = 1
    winnings = 0
    for row in ordered_hands:
        for hand in row:
            winnings+=hand_bid[hand]*rank
            rank+=1
    print(winnings)
main()
