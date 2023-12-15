from collections import defaultdict

with open( 'Day15Input.txt' ) as f:
    line = f.read().splitlines()

line = line[ 0 ].split( ',' )

def part1():
    total = 0
    for string in line:
        currValue = 0
        for ch in string:
            asciiVal = ord( ch )
            currValue += asciiVal
            currValue *= 17
            currValue %= 256
        total += currValue
    print( 'Part 1:', total ) # 512283

def part2():
    boxes = defaultdict( list )
    for string in line:
        box = 0
        if '=' in string:
            lensFound = False
            string = string.split( '=' )
            label = string[ 0 ]
            focalLength = int( string[ 1 ] )
            for ch in label:
                asciiVal = ord( ch )
                box += asciiVal
                box *= 17
                box %= 256
            for i, _ in enumerate( boxes[ box ] ):
                if boxes[ box ][ i ][ 0 ] == label:
                    lensFound = True
                    boxes[ box ][ i ] = ( label, focalLength )
            if not lensFound:
                boxes[ box ].append( ( label, focalLength ) )
        elif '-' in string:
            label = string.split( '-' )[ 0 ]
            for ch in label:
                asciiVal = ord( ch )
                box += asciiVal
                box *= 17
                box %= 256
            # Create a new dictionary with the labels after removing the "label-" if present
            boxes[ box ] = [ l for l in boxes[ box ] if l[ 0 ] != label ]
    total = 0
    for box, lenses in boxes.items():
        for i, lens in enumerate( lenses ):
            total += ( box + 1 ) * lens[ 1 ] * ( i + 1 )
    print( 'Part 2:', total ) # 215827
part1()
part2()