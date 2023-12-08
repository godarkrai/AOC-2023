from collections import defaultdict, deque
import math

with open( 'Day8Input.txt' ) as f:
    input = f.read().splitlines()

instructions = input[ 0 ]

graph = { from_:to.replace( ')', '' ).replace( '(', '' ).split( ', ' ) for from_, to in ( network.split( ' = ' ) for network in input[ 2: ] ) }
startingNodes = [ from_ for network in input[ 2: ] if ( from_ := network.split( ' = ' )[ 0 ] ).endswith( 'A' ) ]

def getSteps( startingNode = 'AAA' ):
    q = deque( [ ( startingNode, 0, instructions[ 0 ] ) ] )
    index = 0
    while q:
        currentNode, totalSteps, currentInstruction = q.popleft()
        if currentNode.endswith( 'Z' ):
            return totalSteps
        if currentNode in graph:
            node1, node2 = graph[ currentNode ]
            index = ( index + 1 ) % ( len( instructions ) )
            if currentInstruction == 'L':
                q.append( ( node1, totalSteps + 1, instructions[ index ] ) )
            else:
                q.append( ( node2, totalSteps + 1, instructions[ index ] ) )

ret = 1
for startingNode in startingNodes:
    ret = math.lcm( ret, getSteps( startingNode ) )
    # Get all the end points of various nodes and then LCM

print( 'Part 1:', getSteps() ) # Part 1: 20569
print( 'Part 2:', ret ) # Part 2: 21366921060721