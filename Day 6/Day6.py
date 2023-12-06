from math import log

with open( 'Day6Input.txt' ) as f:
    input = f.read().splitlines()

times = [ *map(int, input[ 0 ].split()[ 1: ] ) ]
records = [ *map( int, input[ 1 ].split()[ 1: ] ) ]

# FOR PART 2
singleTime = 0
# Combine Times
for time in times:
    singleTime = singleTime*10**int( log( time, 10 )+1 )+time

singleRecord = 0
# Combine Records
for record in records:
    singleRecord = singleRecord*10**int( log( record, 10 ) + 1 ) + record

def part1():
    # Lets do brute force for first part
    # If you hold the button down for all the time duration, you will travel 0
    # So travel[0] and travel[-1] == 0 for time = 0 or time = maxTime
    # if you hold for 1 millisecond the boat's speed would be equal to the time we held the button
    # For T = 1, Speed = 1, total Distance = timeRemaining * speed => ( 7 - T ) * 1 => ( 7 - 1 ) * 6 => 6
    # For T = 2, Speed = 2, totalDistance = ( 7 - 2 ) * 2 => 10
    # Brute Forced
    # T: O( N * M ) where N is the length of times array and M is the total time
    totalWins = 1
    for i in range( len( times ) ):
        currentWins = 0
        for j in range( times[ i ]+1 ): # We have to include the start and end time
            # timeHeldButton = j
            # speedOfTheBoat = timeHeldButton
            totalDistanceTravelled = ( times[ i ] - j ) * j
            if totalDistanceTravelled > records[ i ]:
                currentWins += 1
        totalWins *= currentWins
    return totalWins

def part2():
    # Lets try to optimize it with Binary Search

    # The thought process is that we can split it into two binary searches.
    # Find the Mid number, left of that mid would be the left search area and right would be the right
    mid = ( singleTime + 1 ) // 2

    def isNewRecord( time ):
        totalDistanceTravelled = ( singleTime - time ) * time
        if totalDistanceTravelled > singleRecord:
            return True
        return False

    # For the lower value:
    left = 0
    right = mid

    while left < right:
        newMid = ( left + right ) // 2
        if isNewRecord( newMid ):
            right = newMid
        else:
            left = newMid + 1

    lowestTime = left
    
    # For the Higher value
    left = mid
    right = singleTime + 1

    while left < right:
        newMid = ( left + right ) // 2
        if isNewRecord( newMid ):
            left = newMid + 1
        else:
            right = newMid

    highestTime = right
    return highestTime - lowestTime

print( 'Part 1:', part1() ) # Part 1: 625968
print( 'Part 2:', part2() ) # Part 2: 43663323