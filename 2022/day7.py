def main():
    """
    fs
    """
    with open("input", "r", encoding="utf-8") as f:
        inp = f.readlines()
    counter = 0
    stack = []
    sizes = {}
    while counter!=len(inp):
        line = inp[counter].strip()
        if line.startswith('$ cd ..'):
            stack.pop()
        elif line.startswith('$ cd '):
            directory = line[5:]
            #fix for directories with same name
            j=0
            while True:
                if directory+str(j) not in sizes:
                    sizes[directory+str(j)]=0
                    break
                else:
                    j+=1
            stack.append(directory+str(j))

        elif line.startswith('$ ls'):
            counter+=1
            line = inp[counter].strip()
            while not inp[counter].startswith('$'):
                line = inp[counter].strip()
                if not line.startswith('dir'):
                    for i in stack:
                        sizes[i]+=int(line.split()[0])
                counter+=1
                if counter==len(inp):
                    break
            continue
        counter+=1
    size = 0
    for _,k in enumerate(sizes):
        if sizes[k]<=100000:
            size+=sizes[k]
    print("Part 1: "+str(size))
    needed = 30000000-(70000000-41111105) #from prompt
    for i in sorted(sizes.values()):
        if i>=needed:
            print("Part 2: "+str(i))
            break
if __name__ == '__main__':
    main()
