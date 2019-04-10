import random

# octaves = number of waves
# frequency = ocsillations between high and low
# amplitude = how much each wave is going to affect the total output

from noise import pnoise2, snoise2

#from main import map

print(map)
def simplex(randomSeed, x,y):
    # return -1 to 1
    return (randomSeed.noise2d(x,y)) # use 3d to add a value for solid, empty or else (gold or only rock)



def randomly_populate_map(map, randomSeed, size, octa=1, frequ=16.0):
    #global map
    
    #print(len(map)) #.__dict__)
    
    octaves = octa
    freq = frequ * octaves
    h = len(map[0])
    w = len(map)
    for x in range(w):
        for y in range(h):
            map[x][y].color = int(simplex(randomSeed,x / freq, y / freq) * 127.0 + 128.0)   
    # multiply with 5 more octa! cellular style
    octaves = octa +5
    freq = frequ * octaves
    h = len(map[0])
    w = len(map)
    for x in range(w):
        for y in range(h):
            map[x][y].color = int((map[x][y].color + int(simplex(randomSeed,x / freq, y / freq) * 127.0 + 128.0)    )/2)
    return map
def old_randomly_populate_map(randomSeed, size, octa=1, frequ=16.0):
    global map
    map=[]
    # size = (w,h)
    
    octaves = octa
    freq = frequ * octaves
    for x in range(size[0]):
        row = []
        for y in range(size[1]):
            #row.append(int(snoise2(x / freq, y / freq, octaves) * 127.0 + 128.0))
            #row.append(int(simplex(randomSeed,x / freq, y / freq) * 127.0 + 128.0))
            row.append(int(simplex(randomSeed,x / freq, y / freq) * 127.0 + 128.0))
        map.append(row)
    """
    print(map)
    out = []
    h = len(map[0])
    w = len(map)
    for x in range(w):
        #row = []
        for y in range(h):
            map[x][y] = int(snoise2(x / freq, y / freq, octaves) * 127.0 + 128.0)
            #simplex(randomSeed,x,y)
            #row.append(simplex(seed,x,y))
        #map.append(row)
    """
    return map
