from heapq import heappop
from heapq import heappush

with open( 'Day17Input.txt' ) as f:
    lines = f.read().splitlines()

grid = [ ]
for l in lines:
    grid.append( list( map( int, [ *l ] ) ) )

directionsValues = {
    'D': (1, 0),
    'U': (-1, 0),
    'R': (0, 1),
    'L': (0, -1)
}


def solve( min, max ):
    currentPoint = (0, 0)
    currentHeatValue = 0
    heap = [ ]
    heappush( heap, (currentHeatValue, currentPoint, 1, directionsValues[ 'R' ]) )
    heappush( heap, (currentHeatValue, currentPoint, 1, directionsValues[ 'D' ]) )
    visited = set()
    rows = len( grid )
    cols = len( grid[ 0 ] )
    end = (rows - 1, cols - 1)
    while heap:
        currentHeatValue, currentPoint, steps, direction = heappop( heap )
        if (currentPoint, steps, direction) in visited:
            continue
        visited.add( (currentPoint, steps, direction) )
        newX = currentPoint[ 0 ] + direction[ 0 ]
        newY = currentPoint[ 1 ] + direction[ 1 ]
        if newX < 0 or newX > rows - 1 or newY < 0 or newY > cols - 1:
            continue
        newCost = currentHeatValue + grid[ newX ][ newY ]
        if min <= steps <= max:
            if (newX, newY) == end:
                return newCost
        for d in [ (1, 0), (0, 1), (-1, 0), (0, -1) ]:
            # Cant go back
            if d[ 0 ] + direction[ 0 ] == 0 and d[ 1 ] + direction[ 1 ] == 0:
                continue
            # If previous direction is equal to the current direction, increase step count else reset
            newSteps = steps + 1 if d == direction else 1
            # if the new direction is not equal to the current direction and we are below the min steps we must
            # take with the new direction then don't push this new direction or if have traversed more than the
            # limit in the same direction then don't push too
            if (d != direction and steps < min) or newSteps > max:
                continue
            # We must move in the same direction for 4 steps before turning
            heappush( heap, (newCost, (newX, newY), newSteps, d) )
            # 887 too low


print( solve( 1, 3 ) )  # 758
print( solve( 4, 10 ) )  # 892
