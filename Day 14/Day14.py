from copy import deepcopy

with open( 'Day14Input.txt' ) as f:
    lines = f.read().splitlines()

def moveRockUntilNorthFace( row, col ):
    for r in range( row, 0, -1 ):
        # If the cell above is either 'O' or '#' don't move the rock
        if newGrid[ r - 1 ][ col ] in 'O#':
            # Dont Move
            newGrid[ r ][ col ] = 'O'
            return
        if newGrid[ r - 1 ][ col ] == '.':
            newGrid[ r ][ col ] = '.'
            newGrid[ r - 1 ][ col ] = 'O'


def moveRockUntilWestFace( row, col ):
    # col -= 1
    for c in range( col, 0, -1 ):
        # If the cell to the left is either 'O' or '#' don't move the rock
        if newGrid[ row ][ c - 1 ] in 'O#':
            # Dont Move
            newGrid[ row ][ c ] = 'O'
            return
        if newGrid[ row ][ c - 1 ] == '.':
            newGrid[ row ][ c ] = '.'
            newGrid[ row ][ c - 1 ] = 'O'


def moveRockUntilSouthFace( row, col ):
    for r in range( row, R - 1 ):
        # If the cell down is either 'O' or '#' don't move the rock
        if newGrid[ r + 1 ][ col ] in 'O#':
            # Dont Move
            newGrid[ r ][ col ] = 'O'
            return
        if newGrid[ r + 1 ][ col ] == '.':
            newGrid[ r ][ col ] = '.'
            newGrid[ r + 1 ][ col ] = 'O'


def moveRockUntilEastFace( row, col ):
    for c in range( col, C - 1 ):
        # If the cell down is either 'O' or '#' don't move the rock
        if newGrid[ row ][ c + 1 ] in 'O#':
            # Dont Move
            newGrid[ row ][ c ] = 'O'
            return
        if newGrid[ row ][ c + 1 ] == '.':
            newGrid[ row ][ c ] = '.'
            newGrid[ row ][ c + 1 ] = 'O'


def solve( grid, part ):
    visited = {}
    i = 0
    while i < 10 ** 9:
        i += 1
        for row in range( 1, R ):
            for col in range( C ):
                if grid[ row ][ col ] == 'O':
                    moveRockUntilNorthFace( row, col )
        if part != 2:
            return
        grid = deepcopy( newGrid )
        for col in range( 1, C ):
            for row in range( R ):
                if grid[ row ][ col ] == 'O':
                    moveRockUntilWestFace( row, col )
        grid = deepcopy( newGrid )
        for row in range( R - 1, -1, -1 ):
            for col in range( C ):
                if grid[ row ][ col ] == 'O':
                    moveRockUntilSouthFace( row, col )
        grid = deepcopy( newGrid )
        for col in range( C - 1, -1, -1 ):
            for row in range( R ):
                if grid[ row ][ col ] == 'O':
                    moveRockUntilEastFace( row, col )
        grid = deepcopy( newGrid )
        string = ''
        for nRow in newGrid:
            string += ''.join(nRow)
        if string in visited:
            # If we find this pattern before we jump with this formula
            cycleLength = i - visited[ string ]
            amount = (10**9-i) // cycleLength
            i += amount * cycleLength
        visited[ string ] = i

# ======== Part 1 =========== #
grid = [ ]
for l in lines:
    grid.append( [ *l ] )
newGrid = deepcopy( grid )
R = len( grid )
C = len( grid[ 0 ] )
solve( grid, 1 )
currentRow = R
total = 0
for row in range( R ):
    for col in range( C ):
        if newGrid[ row ][ col ] == 'O':
            total += currentRow
    currentRow -= 1
print( 'Part 1:', total )  # Part 1: 102497

# ======== Part 2 =========== #
grid = [ ]
for l in lines:
    grid.append( [ *l ] )
newGrid = deepcopy( grid )
solve( grid, 2 )
currentRow = R
total = 0
for row in range( R ):
    for col in range( C ):
        if newGrid[ row ][ col ] == 'O':
            total += currentRow
    currentRow -= 1
print( 'Part 2:', total )  # Part 2: 105008