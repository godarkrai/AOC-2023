from collections import defaultdict

with open( 'Day4Input.txt' ) as f:
    input = f.read().splitlines()

def part1():
    total = 0
    for line in input:
        currentTotal = 1
        line = line.split( ':' )[ 1 ]
        allNumbers = line.split( '|' )
        cardNumbers = allNumbers[ 0 ].split( ' ' )
        winningNumbers = allNumbers[ 1 ].split( ' ' )
        
        multiplyWith = 1

        for number in cardNumbers:
            if number == '':
                continue
            if number in winningNumbers:
                currentTotal *= multiplyWith
                if multiplyWith == 1:
                    multiplyWith = 2
        if multiplyWith == 2:
            total += currentTotal
    return total

def part2():
    cardCount = defaultdict( int )
    for line in input:
        totalGames = 0
        line = line.split( ':' )
        game = int( line[ 0 ].split( ' ' )[ -1 ] )
        cardCount[ game ] += 1
        allNumbers = line[ 1 ].split( '|' )
        cardNumbers = allNumbers[ 0 ].split( ' ' )
        winningNumbers = allNumbers[ 1 ].split( ' ' )
        for number in cardNumbers:
            if number == '':
                continue
            if number in winningNumbers:
                totalGames += 1
        for g in range( game + 1, game + 1 + totalGames ):
            # We add the amount of cards with the previous amount
            # Lets say we have 2 cards of Game 2 and if we have 3 matching numbers then
            # Game 3, Game 4 and Game 5 would have extra cards equal to the amount of current
            # Game 2 card so that means they would be incremented by 2 which is nothing but cardCount[ 2 ]
            cardCount[ g ] += cardCount[ game ]
    return sum( cardCount.values() )

print( 'Part 1:', part1() ) # 23941
print( 'Part 2:', part2() ) # 5571760
