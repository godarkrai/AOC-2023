with open( 'Day3Input.txt' ) as f:
    input = f.read().splitlines()

matrix = []
for line in input:
    curLine = [ *line ]
    matrix.append( curLine )

ROWS = len( matrix )
COLS = len( matrix[ 0 ] )
directions = [ ( 1,0 ), ( -1, 0 ), ( 0,1 ), ( 0,-1 ), ( 1, -1 ), ( -1, 1 ), ( 1, 1 ), ( -1, -1 ) ]

def getNumber( visited, row, col ):
    currentNumber = matrix[ row ][ col ]
    for c in range( col + 1, COLS ):
        if matrix[ row ][ c ].isnumeric():
            visited.add( ( row, c ) )
            currentNumber += matrix[ row ][ c ]
        else:
            break
    for c in range( col - 1, -1, -1 ):
        if matrix[ row ][ c ].isnumeric():
            visited.add( ( row, c ) )
            currentNumber = matrix[ row ][ c ] + currentNumber
        else:
            break
    return currentNumber

def solve( forPart2 = False ):
    visited = set()
    total = 0
    toSearch = '@#$%&*+/=-' if not forPart2 else '*'
    for row in range( ROWS ):
        for col in range( COLS ):
            if forPart2:
                currentProduct = 1
                gearCount = 0
            if matrix[ row ][ col ] in toSearch:
                for direction in directions:
                    newRow = row + direction[ 0 ]
                    newCol = col + direction[ 1 ]
                    if ( newRow, newCol ) not in visited and matrix[ newRow ][ newCol ].isnumeric():
                        visited.add( ( newRow, newCol ) )
                        number = getNumber( visited, newRow, newCol )
                        if forPart2:
                            gearCount += 1
                            currentProduct *= int( number )
                        else:
                            total += int( number )
            if forPart2 and gearCount == 2:
                total += currentProduct
    return total

print( 'Part 1:', solve() ) # 527144
print( 'Part 2:', solve( True ) ) # 81463996
