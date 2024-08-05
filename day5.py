"""
Day 5 part one Advent of Code
"""
def extract(inp):
    """
    Returns mapping of seed to location for one seed
    """
    #seeds
    pointer = 0
    seeds = inp[pointer].split(":")[1].split()
    for i in enumerate(seeds):
        seeds[i]=int(seeds[i])
    #seed to soil
    pointer = 3
    seedsoil, pointer = extract_helper(pointer, inp)
    #soil to fertilizer
    pointer +=2
    soilfertilizer, pointer = extract_helper(pointer, inp)
    #fertilizer to water
    pointer +=2
    fertilizerwater, pointer = extract_helper(pointer, inp)
    #water to light
    pointer +=2
    waterlight, pointer = extract_helper(pointer, inp)
    #light to temp
    pointer +=2
    lighttemp, pointer = extract_helper(pointer, inp)
    #temp to humidity
    pointer +=2
    temphumidity, pointer = extract_helper(pointer, inp)
    #humidity to location
    pointer +=2
    humiditylocation, pointer = extract_helper(pointer, inp)
    return seeds, seedsoil, soilfertilizer, fertilizerwater, waterlight, lighttemp, temphumidity, humiditylocation
    
def main():
    """
    Reads file and prints locations per seed
    """
    with open("input.txt", "r", encoding="utf-8") as f:
    inp = f.read()
    inp = inp.split("\n")
    seeds, seedsoil, soilfertilizer, fertilizerwater, waterlight, lighttemp, temphumidity, humiditylocation = extract(inp)
    locs = []
    for seed in seeds:
        soil = convert(seed, seedsoil)
        fertilizer = convert(soil, soilfertilizer)
        water = convert(fertilizer, fertilizerwater)
        light = convert(water, waterlight)
        temp = convert(light, lighttemp)
        humidity = convert(temp, temphumidity)
        location = convert(humidity, humiditylocation)
        locs.append(location)
    locs.sort()
    print(locs[0])
    return 0

def extract_helper(pointer, inp):
    """
    Helper function that helps map one variable to another
    """
    l1 = []
    while inp[pointer]!='':
        l1.append(inp[pointer].split())
        pointer+=1
        if pointer==len(inp):
            break
    for i in enumerate(l1):
        for j in enumerate(l1[i]):
            l1[i][j] = int(l1[i][j])
    return l1, pointer

def convert(src, dst_list):
    """
    Traversal of list to find required destination. If not found, return original
    """
    for i in dst_list:
        if i[1]<=src<=i[1]+i[2]:
            return i[0]+(src-i[1])
    return src

if __name__ == '__main__':
    main()
