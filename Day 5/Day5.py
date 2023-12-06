with open( 'Day5Input.txt' ) as f:
    input = f.read().splitlines()

N = len( input )
seeds = [ *map(int, input[ 0 ].split( ': ' )[ 1 ].split()) ]
maps = []
i = 3
currentMap = []
while i < N:
    if len( input[ i ] ) == 0:
        maps.append( currentMap )
        currentMap = []
        i += 2
        continue
    mapping = input[ i ].split( ' ' )
    dest  = int( mapping[ 0 ] )
    mapStart = int( mapping[ 1 ] )
    mapEnd = mapStart + int( mapping[ 2 ] )
    currentMap.append( [ dest, mapStart, mapEnd ] )
    i += 1

# For the last map
maps.append( currentMap )

def part1():
    locations = []
    for curr in seeds:
        for map_ in maps:
            for ( destStart, mapStart, mapEnd ) in map_:
                if mapStart <= curr <= mapEnd:
                    curr = destStart + curr - mapStart
                    break
        locations.append( curr )
    return min( locations )

def part2():
    locations = []
    seedPairs = []
    for i in range(0, len(seeds), 2):
        seedPairs.append( [ seeds[i], seeds[i] + seeds[i+1] ])
    
    for pair in seedPairs:
        # Only proceed when total overlap
        pairs = [ pair ]
        results = []

        for map_ in maps:
            while pairs:
                rangeStart, rangeEnd = pairs.pop() # Lets say current is range x-y and the map range is a-b
                for destStart, mapStart, mapEnd in map_:
                    offset = destStart - mapStart
                    if mapEnd <= rangeStart or rangeEnd <= mapStart:  # no overlap a-b-x-y or x-y-a-b
                        continue
                    if rangeStart < mapStart: # x-a-y-b
                        pairs.append( [ rangeStart, mapStart ] )
                        rangeStart = mapStart
                    if mapEnd < rangeEnd: # a-x-b-y
                        pairs.append( [ mapEnd, rangeEnd ] )
                        rangeEnd = mapEnd
                    results.append( [ rangeStart + offset, rangeEnd + offset ])
                    break
                else:
                    results.append( [ rangeStart, rangeEnd ] )
            pairs = results
            results = []
        locations += pairs
    return min( loc[0] for loc in locations )
print( part1() ) # 251346198
print( part2() ) # 72263011