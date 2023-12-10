from collections import deque

with open( 'Day10Input.txt' ) as f:
    input = f.read().splitlines()

grid = []

start = [ 0,0 ]
for i, gridLines in enumerate( input ):
    if 'S' in gridLines:
        start = [ i, gridLines.find( 'S' ) ]
    grid.append( [ *gridLines ] )

directions = [ ( 1,0 ), ( 0,1 ), ( -1,0 ), ( 0,-1 ) ]

def part1():
    def canGoUp( row, col ):
        if grid[ row ][ col ] in '|JLS':
            return True
        return False

    def canReceiveFromDown( row, col ):
        if grid[ row ][ col ] in '|F7S':
            return True
        return False

    def canGoLeft( row, col ):
        if grid[ row ][ col ] in '-J7S':
            return True
        return False

    def canReceiveFromRight( row, col ):
        if grid[ row ][ col ] in '-LFS':
            return True
        return False

    def canGoRight( row, col ):
        if grid[ row ][ col ] in '-LFS':
            return True
        return False

    def canReceiveFromLeft( row, col ):
        if grid[ row ][ col ] in '-J7S':
            return True
        return False

    def canGoDown( row, col ):
        if grid[ row ][ col ] in '|F7S':
            return True
        return False

    def canReceiveFromUp( row, col ):
        if grid[ row ][ col ] in 'JL|S':
            return True
        return False

    def validCell( row, col ):
        return row >= 0 and row < len( grid ) and col >= 0 and col < len( grid[ 0 ] )

    # Basically BFS from the start point to all the points and get the min( maxDistance )
    newGrid = [ [ 0 for _ in range( len( grid[0] ) ) ] for _ in range( len( grid ) ) ]
    visited = set()
    visited.add( ( start[0],start[1] ) )
    def bfs():
        q = deque()
        q.append( ( start, 0 ) )
        while q:
            ( x,y ), distance = q.popleft()
            if newGrid[ x ][ y ] == 0:
                newGrid[ x ][ y ] = distance
            else:
                newGrid[ x ][ y ] = min( newGrid[ x ][ y ], distance )
            visited.add( ( x, y ) )
            # i = 0: Down, i = 1: Right, i = 2: Up, i = 3: Left
            for i, ( nx, ny ) in enumerate( directions ):
                newRow = x + nx
                newCol = y + ny
                if ( newRow,newCol ) not in visited and validCell( newRow, newCol ):
                    if i == 0: # Going Down: Check if the current cell can go down and the new cell can receive from up
                        if canGoDown( x,y ) and canReceiveFromUp( newRow, newCol ):
                            q.append( ( [ newRow, newCol ], distance + 1 ) )
                    elif i == 1: # Goind Right: Check if the current cell can go right and the new cell can receive from left
                        if canGoRight( x,y ) and canReceiveFromLeft( newRow, newCol ):
                            q.append( ( [ newRow, newCol ], distance + 1 ) )
                    elif i == 2: # Going Up: Check if the current cell can go up and the new cell can receive from down
                        if canGoUp( x,y ) and canReceiveFromDown( newRow, newCol ):
                            q.append( ( [ newRow, newCol ], distance + 1 ) )
                    else: # Going Left
                        if canGoLeft( x,y ) and canReceiveFromRight( newRow, newCol ):
                            q.append( ( [ newRow, newCol ], distance + 1 ) )
    bfs()
    return newGrid

newGrid = part1()
max_ = float( '-inf' )
for nGrid in newGrid:
    max_ = max( max_, max( nGrid ) )
print( 'Part 1:', max_ ) # Part 1: 6956

def part2():

    def validCell( row, col ):
        return row >= 0 and row < len( blownUpMaze ) and col >= 0 and col < len( blownUpMaze[ 0 ] )
    '''
    Blow up the maze, change single characters to this
    Make L => .|.
              .L-
              ...
    '''
    R = len( grid )
    C = len( grid[ 0 ] )
    '''
    Change S to a proper sign by looking at neighbouring values
    '''
    for r in range( R ):
        for c in range( C ):
            if grid[ r ][ c ] =='S':
                upValid = ( grid[ r-1 ][ c ] in [ '|','7','F' ] )
                rightValid = ( grid[ r ][ c+1 ] in [ '-','7','J' ] )
                downValid = ( grid[ r+1 ][ c ] in [ '|','L','J' ] )
                leftValid = ( grid[ r ][ c-1 ] in [ '-','L','F' ] )
                if upValid and downValid:
                    grid[ r ][ c ] = '|'
                elif upValid and rightValid:
                    grid[ r ][ c ] = 'L'
                elif upValid and leftValid:
                    grid[ r ][ c ] = 'J'
                elif downValid and rightValid:
                    grid[ r ][ c ] = 'F'
                elif downValid and leftValid:
                    grid[ r ][ c ] = '7'
                elif leftValid and rightValid:
                    grid[ r ][ c ] = '-'
                
    blownUpMaze = [ [ '.' for _ in range( len( grid[0] ) * 3 ) ] for _ in range( len( grid ) * 3 ) ]
    for row in range( R ):
        for col in range( C ):
            blownUpRow = row * 3
            blownUpCol = col * 3
            if grid[ row ][ col ] == '|':
                blownUpMaze[ blownUpRow + 0 ][ blownUpCol + 1 ] = 'x'
                blownUpMaze[ blownUpRow + 1 ][ blownUpCol + 1 ] = 'x'
                blownUpMaze[ blownUpRow + 2 ][ blownUpCol + 1 ] = 'x'
            elif grid[ row ][ col ] == 'F':
                blownUpMaze[ blownUpRow + 1 ][ blownUpCol + 1 ] = 'x'
                blownUpMaze[ blownUpRow + 1 ][ blownUpCol + 2 ] = 'x'
                blownUpMaze[ blownUpRow + 2 ][ blownUpCol + 1 ] = 'x'
            elif grid[ row ][ col ] == 'L':
                blownUpMaze[ blownUpRow + 0 ][ blownUpCol + 1 ] = 'x'
                blownUpMaze[ blownUpRow + 1 ][ blownUpCol + 1 ] = 'x'
                blownUpMaze[ blownUpRow + 1 ][ blownUpCol + 2 ] = 'x'
            elif grid[ row ][ col ] == 'J':
                blownUpMaze[ blownUpRow + 1 ][ blownUpCol + 1 ] = 'x'
                blownUpMaze[ blownUpRow + 0 ][ blownUpCol + 1 ] = 'x'
                blownUpMaze[ blownUpRow + 1 ][ blownUpCol + 0 ] = 'x'
            elif grid[ row ][ col ] == '-':
                blownUpMaze[ blownUpRow + 1 ][ blownUpCol + 2 ] = 'x'
                blownUpMaze[ blownUpRow + 1 ][ blownUpCol + 1 ] = 'x'
                blownUpMaze[ blownUpRow + 1 ][ blownUpCol + 0 ] = 'x'
            elif grid[ row ][ col ] == '7':
                blownUpMaze[ blownUpRow + 1 ][ blownUpCol + 0 ] = 'x'
                blownUpMaze[ blownUpRow + 1 ][ blownUpCol + 1 ] = 'x'
                blownUpMaze[ blownUpRow + 2 ][ blownUpCol + 1 ] = 'x'
    
    # Flood Fill from boundary points
    q = deque()
    visited = set()
    for r in range( len( blownUpMaze ) ):
        q.append( ( r, 0 ) ) # First Column of every Row
        q.append( ( r, len( blownUpMaze[ 0 ] ) - 1 ) ) # Last column of every row
    for c in range( len( blownUpMaze[ 0 ] ) ):
        q.append( ( 0, c ) )
        q.append( ( len( blownUpMaze ) - 1, c ) )
    
    while q:
        x, y = q.popleft()
        if not validCell( x, y ):
            continue
        if ( x,y ) in visited or blownUpMaze[ x ][ y ] == 'x':
            continue
        visited.add( ( x, y) )
        blownUpMaze[ x ][ y ] = '0'
        for ( nx, ny ) in directions:
            q.append( ( x + nx, y + ny ) )

    ans = 0
    for row in range( R ):
        for col in range( C ):
            seen = False
            for rr in [ 0,1,2 ]:
                for cc in [ 0,1,2 ]:
                    if ( 3*row+rr, 3*col+cc ) in visited:
                        seen = True
            if not seen:
                ans += 1
    return ans
print( 'Part 2:', part2() ) # 455