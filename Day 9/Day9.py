with open( 'Day9Input.txt' ) as f:
    input = f.read().splitlines()

def solve( part = 1 ):
    total = 0
    for seq in input:
        seqToArray = list( map( int, seq.split( ' ' ) ) )
        if part == 2:
            seqToArray = seqToArray[ ::-1 ]
        lastVariables = []
        while set( seqToArray ) != set( [0] ):
            for i in range( len( seqToArray ) - 1 ):
                seqToArray[ i ] = seqToArray[ i + 1 ] - seqToArray[ i ]
            lastVariables.append( seqToArray.pop( -1 ) )
        total += sum( lastVariables )
    return total
print( 'Part 1:', solve() ) # 2174807968
print( 'Part 2:', solve( 2 ) ) # 1208