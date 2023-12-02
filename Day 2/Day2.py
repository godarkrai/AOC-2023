with open( 'Day2Input.txt' ) as f:
    input = f.read().splitlines()

def part1():
    totalGames = 0
    max = {
        'blue': 14,
        'green': 13,
        'red': 12
    }
    for line in input:
        line = line.split( ':' )
        game = line[ 0 ].split( ' ' )[ 1 ]
        badGame = False
        cubes = line[ 1 ].split( ';' )
        for cube in cubes:
            cube = cube[ 1: ]
            cube = cube.split( ', ' )
            for colorCube in cube:
                count, color = colorCube.split( ' ' )
                if int( count ) > max[ color ]:
                    badGame = True
                    break
            if badGame:
                break
        if not badGame:
            totalGames += int( game )
    return totalGames

def part2():
    # Fetch max color count for each game
    total = 0
    for line in input:
        line = line.split( ':' )
        cubes = line[ 1 ].split( ';' )
        currentMax = {
            'red': float( '-inf' ),
            'blue': float( '-inf' ),
            'green': float( '-inf' )
        }
        for cube in cubes:
            cube = cube[ 1: ]
            cube = cube.split( ', ' )
            for colorCube in cube:
                count, color = colorCube.split( ' ' )
                if int( count ) > currentMax[ color ]:
                    currentMax[ color ] = int( count )
        curTotal = 1
        for maxColorCount in currentMax.values():
            curTotal *= maxColorCount
        total += curTotal
    return total

print( 'Part 1:', part1() ) # Part 1: 3059
print( 'Part 2:', part2() ) # Part 2: 65371