with open("input.txt", "r") as f:
    inp = f.readlines()
for i in range(0, len(inp)):
    inp[i] = [x for x in inp[i]]
    inp[i].pop(-1)
    #print(inp[i])

def main():
    sum = 0
    for i in range(0, len(inp)):
        for j in range(0,len(inp[i])):
            if inp[i][j].isdigit():
                sum += checkAdj(inp, i,j, 1)
    print(sum)
    ratio = 0
    for key in d1.keys():
        if len(d1[key])==2:
            ratio+=d1[key][0]*d1[key][1]
    print(ratio)
def checkAdj(l1, i,j, replace):
    num = l1[i][j]
    tmpIndex=j+1
    while tmpIndex<len(inp[i]):
        if l1[i][tmpIndex].isdigit():
            num+=l1[i][tmpIndex]
        else:
            break
        tmpIndex+=1
    numsize = len(num)
    num = int(num)
    sym = 0
    symX, symY = 0,0
    for k in range(j,j+numsize):
        inp[i][k]='.'
    #left
    if j>0 and sym == 0:
        if l1[i][j-1]!='.':
            sym = 1
            symX, symY = i, j-1
            update(num, symX, symY)
            #print(l1[i][j-1])
            #l1[i][j-1]='.'
    #top left
    if j>0 and i>0 and sym == 0:
        if l1[i-1][j-1]!='.':
            sym = 1
            symX, symY = i-1, j-1
            update(num, symX, symY)
            #print(l1[i][j-1])
            #l1[i][j-1]='.'
    #top middle
    if i>0 and sym==0:
        for ind in range(j,j+numsize):
            if l1[i-1][ind]!='.':
                sym = 1
                symX, symY = i-1, ind
                update(num, symX, symY)
                #print(l1[i-1][ind])
                #l1[i-1][ind]='.'
                break
    #top right
    if j+numsize<len(inp[i]) and i>0 and sym == 0:
        if l1[i-1][j+numsize]!='.':
            symX, symY = i-1, j+numsize
            update(num, symX, symY)
            sym = 1
            #print(l1[i-1][j+numsize])
            #l1[i-1][j+numsize]='.'
    #right
    if j+numsize<len(inp[i]) and sym == 0:
        if l1[i][j+numsize]!='.':
            sym = 1
            symX, symY = i, j+numsize
            update(num, symX, symY)
            #print(l1[i][j+numsize])
            #l1[i][j+numsize]='.'
    #bottom left
    if i+1<len(inp) and j>0 and sym == 0:
        if l1[i+1][j-1]!='.':
            sym = 1
            symX, symY = i+1, j-1
            update(num, symX, symY)
            #print(l1[i+1][j-1])
            #l1[i+1][j-1]='.'
    #bottom middle
    if i+1<len(inp) and sym ==0:
        for ind in range(j,j+numsize):
            if l1[i+1][ind]!='.':
                sym = 1
                symX, symY = i+1, ind
                update(num, symX, symY)
                #print(l1[i+1][ind])
                #l1[i+1][ind]='.'
                break
    #bottom right
    if i+1<len(inp) and j+numsize<len(inp[i]) and sym == 0:
        if l1[i+1][j+numsize]!='.':
            sym = 1
            symX, symY = i+1, j+numsize
            update(num, symX, symY)
            #print(l1[i+1][j+numsize])
            #l1[i+1][j+numsize]='.'
    if sym == 0:
        #print(num)
        return 0
    return num

d1 = {}
def update(num,i,j):
    key=str(i)+","+str(j)
    if key not in d1:
        d1[key]=[num]
    else:
        d1[key].append(num)
main()
