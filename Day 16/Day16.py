from collections import deque
from copy import deepcopy

with open( 'Day16Input.txt' ) as f:
    lines = f.read().splitlines()

grid = []
for line in lines:
    grid.append( [ *line ] )

directions = {
    '>': ( 0,1 ),
    'V': ( 1,0 ),
    '^': ( -1,0 ),
    '<': ( 0,-1 )
}

R = len( grid )
C = len( grid[ 0 ] )

def validCell( x,y ):
    if 0 <= x < R and 0 <= y < C:
        return True
    return False

def part1():
    newGrid = [ [ 0 ] * C for _ in range( R ) ]
    visited = set()
    startingPoint = ( 0,0 )
    startingDirection = '>'
    if grid[ 0 ][ 0 ] == '\\':
        startingDirection = 'V'
    elif grid[ 0 ][ 0 ] == '/':
        startingDirection = '^'
    visited.add( ( startingPoint, startingDirection ) )
    q = deque()
    q.append( ( startingPoint, startingDirection ) )
    while q:
        currentPoint, currentDir = q.popleft()
        x, y = currentPoint
        if newGrid[ x ][ y ] > 0:
            newGrid[ x ][ y ] += 1
        else:
            newGrid[ x ][ y ] = 1
        nX = directions[ currentDir ][ 0 ]
        nY = directions[ currentDir ][ 1 ]
        if validCell( x + nX, y + nY ):
            newX, newY = x + nX, y + nY
            newPoint = ( newX, newY )
            if ( newPoint, currentDir ) in visited:
                continue
            visited.add( ( newPoint, currentDir ) )
            if currentDir == '>':
                if grid[ newX ][ newY ] == '|':
                    # Split the beam into two, 
                    q.append( ( newPoint, 'V' ) )
                    q.append( ( newPoint, '^' ) )
                elif grid[ newX ][ newY ] == '/':
                    # No change, keep moving forward
                    q.append( ( newPoint, '^' ) )
                elif grid[ newX ][ newY ] == '\\':
                    q.append( ( newPoint, 'V' ) )
                else: # For '-', any beam, '.'
                    q.append( ( newPoint, '>' ) )
            elif currentDir == '<':
                if grid[ newX ][ newY ] == '|':
                    # Split the beam into two, 
                    q.append( ( newPoint, 'V' ) )
                    q.append( ( newPoint, '^' ) )
                elif grid[ newX ][ newY ] == '/':
                    # No change, keep moving forward
                    q.append( ( newPoint, 'V' ) )
                elif grid[ newX ][ newY ] == '\\':
                    q.append( ( newPoint, '^' ) )
                else: # For '-', any beam, '.'
                    q.append( ( newPoint, '<' ) )
            elif currentDir == 'V':
                if grid[ newX ][ newY ] == '-':
                    # Split the beam into two
                    q.append( ( newPoint, '>' ) )
                    q.append( ( newPoint, '<' ) )
                elif grid[ newX ][ newY ] == '/':
                    # No change, keep moving forward
                    q.append( ( newPoint, '<' ) )
                elif grid[ newX ][ newY ] == '\\':
                    q.append( ( newPoint, '>' ) )
                else: # For '|', AnyBeam, '.'
                    q.append( ( newPoint, 'V' ) )
            else:
                if grid[ newX ][ newY ] == '-':
                    # Split the beam into two
                    q.append( ( newPoint, '>' ) )
                    q.append( ( newPoint, '<' ) )
                elif grid[ newX ][ newY ] == '/':
                    # No change, keep moving forward
                    q.append( ( newPoint, '>' ) )
                elif grid[ newX ][ newY ] == '\\':
                    q.append( ( newPoint, '<' ) )
                else: # For '|', AnyBeam, '.'
                    q.append( ( newPoint, '^' ) )
    total = 0
    for g in newGrid:
        for cell in g:
            if cell > 0:
                total += 1
    print( 'Part 1:', total )
part1()  # 7562

def part2():
    maxTotal = float( '-inf' )
    startingPointsWithDir = []
    for row in range( R ):
        startingPointsWithDir.append( ( ( row, 0 ), '>' ) )
        startingPointsWithDir.append( ( ( row, C-1 ), '<' ) )
    for col in range( C ):
        startingPointsWithDir.append( ( ( 0, col ), 'V' ) )
        startingPointsWithDir.append( ( ( R-1, col ), '^' ) )
    for startingPoint, startingDirection in startingPointsWithDir:
        newGrid = [ [ 0 ] * C for _ in range( R ) ]
        q = deque()
        visited = set()
        x,y = startingPoint
        if grid[ x ][ y ] == '\\':
            if startingDirection == '^':
                startingDirection = '<'
            elif startingDirection == '>':
                startingDirection = 'V'
            elif startingDirection == '<':
                startingDirection = '^'
            elif startingDirection == 'V':
                startingDirection = '>'
            q.append( ( startingPoint, startingDirection ) )
            visited.add( ( startingPoint, startingDirection ) )
        elif grid[ x ][ y ] == '/':
            if startingDirection == '^':
                startingDirection = '>'
            elif startingDirection == '>':
                startingDirection = '^'
            elif startingDirection == '<':
                startingDirection = 'V'
            elif startingDirection == 'V':
                startingDirection = '<'
            q.append( ( startingPoint, startingDirection ) )
            visited.add( ( startingPoint, startingDirection ) )
        elif grid[ x ][ y ] == '-':
            if startingDirection == '^':
                q.append( ( startingPoint, '<' ) )
                visited.add( ( startingPoint, '<' ) )
                q.append( ( startingPoint, '>' ) )
                visited.add( ( startingPoint, '>' ) )
            elif startingDirection == '>':
                startingDirection = '>'
                q.append( ( startingPoint, startingDirection ) )
                visited.add( ( startingPoint, startingDirection ) )
            elif startingDirection == '<':
                startingDirection = '<'
                q.append( ( startingPoint, startingDirection ) )
                visited.add( ( startingPoint, startingDirection ) )
            elif startingDirection == 'V':
                q.append( ( startingPoint, '<' ) )
                visited.add( ( startingPoint, '<' ) )
                q.append( ( startingPoint, '>' ) )
                visited.add( ( startingPoint, '>' ) )
        elif grid[ x ][ y ] == '|':
            if startingDirection == '^':
                startingDirection = '^'
                q.append( ( startingPoint, '^' ) )
                visited.add( ( startingPoint, '^' ) )
            elif startingDirection == '>':
                q.append( ( startingPoint, '^' ) )
                visited.add( ( startingPoint, '^' ) )
                q.append( ( startingPoint, 'V' ) )
                visited.add( ( startingPoint, 'V' ) )
            elif startingDirection == '<':
                q.append( ( startingPoint, '^' ) )
                visited.add( ( startingPoint, '^' ) )
                q.append( ( startingPoint, 'V' ) )
                visited.add( ( startingPoint, 'V' ) )
            elif startingDirection == 'V':
                startingDirection = 'V'
                q.append( ( startingPoint, 'V' ) )
                visited.add( ( startingPoint, 'V' ) )
        else:
            q.append( ( startingPoint, startingDirection ) )
            visited.add( ( startingPoint, startingDirection ) )
        while q:
            currentPoint, currentDir = q.popleft()
            x, y = currentPoint
            if newGrid[ x ][ y ] > 0:
                newGrid[ x ][ y ] += 1
            else:
                newGrid[ x ][ y] = 1
            nX = directions[ currentDir ][ 0 ]
            nY = directions[ currentDir ][ 1 ]
            if validCell( x + nX, y + nY ):
                newX, newY = x + nX, y + nY
                newPoint = ( newX, newY )
                if ( newPoint, currentDir ) in visited:
                    continue
                visited.add( ( newPoint, currentDir ) )
                if currentDir == '>':
                    if grid[ newX ][ newY ] == '|':
                        # Split the beam into two, 
                        q.append( ( newPoint, 'V' ) )
                        q.append( ( newPoint, '^' ) )
                    elif grid[ newX ][ newY ] == '/':
                        # No change, keep moving forward
                        q.append( ( newPoint, '^' ) )
                    elif grid[ newX ][ newY ] == '\\':
                        q.append( ( newPoint, 'V' ) )
                    else: # For '-', any beam, '.'
                        q.append( ( newPoint, '>' ) )
                elif currentDir == '<':
                    if grid[ newX ][ newY ] == '|':
                        # Split the beam into two, 
                        q.append( ( newPoint, 'V' ) )
                        q.append( ( newPoint, '^' ) )
                    elif grid[ newX ][ newY ] == '/':
                        # No change, keep moving forward
                        q.append( ( newPoint, 'V' ) )
                    elif grid[ newX ][ newY ] == '\\':
                        q.append( ( newPoint, '^' ) )
                    else: # For '-', any beam, '.'
                        q.append( ( newPoint, '<' ) )
                elif currentDir == 'V':
                    if grid[ newX ][ newY ] == '-':
                        # Split the beam into two
                        q.append( ( newPoint, '>' ) )
                        q.append( ( newPoint, '<' ) )
                    elif grid[ newX ][ newY ] == '/':
                        # No change, keep moving forward
                        q.append( ( newPoint, '<' ) )
                    elif grid[ newX ][ newY ] == '\\':
                        q.append( ( newPoint, '>' ) )
                    else: # For '|', AnyBeam, '.'
                        q.append( ( newPoint, 'V' ) )
                else:
                    if grid[ newX ][ newY ] == '-':
                        # Split the beam into two
                        q.append( ( newPoint, '>' ) )
                        q.append( ( newPoint, '<' ) )
                    elif grid[ newX ][ newY ] == '/':
                        # No change, keep moving forward
                        q.append( ( newPoint, '>' ) )
                    elif grid[ newX ][ newY ] == '\\':
                        q.append( ( newPoint, '<' ) )
                    else: # For '|', AnyBeam, '.'
                        q.append( ( newPoint, '^' ) )
        total = 0
        for g in newGrid:
            for cell in g:
                if cell > 0:
                    total += 1
        maxTotal = max( maxTotal, total )
    print( 'Part 2:', maxTotal )
part2() # 7793