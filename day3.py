"""
Day 3 of Advent of Code 2023
"""
with open("input.txt", "r", encoding="utf-8") as f:
    inp = f.readlines()
for i in range(0, len(inp)):
    inp[i] = [x for x in inp[i]]
    inp[i].pop(-1)

def main():
    """
    Finds valid parts (numbers adjacent to symbol)
    Also finds symbols adjacent to two numbers and returns sum of their products.
    """
    _sum = 0
    for i in range(0, len(inp)):
        for j in range(0,len(inp[i])):
            if inp[i][j].isdigit():
                _sum += check_adj(inp, i,j, 1)
    print(_sum)
    ratio = 0
    for key in d1.keys():
        if len(d1[key])==2:
            ratio+=d1[key][0]*d1[key][1]
    print(ratio)
def check_adj(l1, i,j):
    """
    Helper function to search for valid parts
    """
    num = l1[i][j]
    tmp_index=j+1
    while tmp_index<len(inp[i]):
        if l1[i][tmp_index].isdigit():
            num+=l1[i][tmp_index]
        else:
            break
        tmp_index+=1
    numsize = len(num)
    num = int(num)
    sym = 0
    sym_x, sym_y = 0,0
    for k in range(j,j+numsize):
        inp[i][k]='.'
    #left
    if j>0 and sym == 0:
        if l1[i][j-1]!='.':
            sym = 1
            sym_x, sym_y = i, j-1
            update(num, sym_x, sym_y)
            #print(l1[i][j-1])
            #l1[i][j-1]='.'
    #top left
    if j>0 and i>0 and sym == 0:
        if l1[i-1][j-1]!='.':
            sym = 1
            sym_x, sym_y = i-1, j-1
            update(num, sym_x, sym_y)
            #print(l1[i][j-1])
            #l1[i][j-1]='.'
    #top middle
    if i>0 and sym==0:
        for ind in range(j,j+numsize):
            if l1[i-1][ind]!='.':
                sym = 1
                sym_x, sym_y = i-1, ind
                update(num, sym_x, sym_y)
                #print(l1[i-1][ind])
                #l1[i-1][ind]='.'
                break
    #top right
    if j+numsize<len(inp[i]) and i>0 and sym == 0:
        if l1[i-1][j+numsize]!='.':
            sym_x, sym_y = i-1, j+numsize
            update(num, sym_x, sym_y)
            sym = 1
            #print(l1[i-1][j+numsize])
            #l1[i-1][j+numsize]='.'
    #right
    if j+numsize<len(inp[i]) and sym == 0:
        if l1[i][j+numsize]!='.':
            sym = 1
            sym_x, sym_y = i, j+numsize
            update(num, sym_x, sym_y)
            #print(l1[i][j+numsize])
            #l1[i][j+numsize]='.'
    #bottom left
    if i+1<len(inp) and j>0 and sym == 0:
        if l1[i+1][j-1]!='.':
            sym = 1
            sym_x, sym_y = i+1, j-1
            update(num, sym_x, sym_y)
            #print(l1[i+1][j-1])
            #l1[i+1][j-1]='.'
    #bottom middle
    if i+1<len(inp) and sym ==0:
        for ind in range(j,j+numsize):
            if l1[i+1][ind]!='.':
                sym = 1
                sym_x, sym_y = i+1, ind
                update(num, sym_x, sym_y)
                #print(l1[i+1][ind])
                #l1[i+1][ind]='.'
                break
    #bottom right
    if i+1<len(inp) and j+numsize<len(inp[i]) and sym == 0:
        if l1[i+1][j+numsize]!='.':
            sym = 1
            sym_x, sym_y = i+1, j+numsize
            update(num, sym_x, sym_y)
            #print(l1[i+1][j+numsize])
            #l1[i+1][j+numsize]='.'
    if sym == 0:
        #print(num)
        return 0
    return num

d1 = {}
def update(num,i,j):
    """
    Helper function to add valid part to a dictionary of parts
    """
    key=str(i)+","+str(j)
    if key not in d1:
        d1[key]=[num]
    else:
        d1[key].append(num)

if __name__ == '__main__':
    main()
