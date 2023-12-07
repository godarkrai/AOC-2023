from collections import defaultdict
with open( 'Day7Input.txt' ) as f:
    input = f.read().splitlines()

# Ranking is based on this sorting criteria
sorting = [ 'high-card', 'one-pair', 'two-pair', 'three-o-a-k', 'full-house', 'four-o-a-k', 'five-o-a-k' ]
hands, bidding = [], {}
for i in input:
    i = i.split( ' ' )
    hand = i[ 0 ]
    hands.append( hand )
    bidding[ hand ] = int( i[ 1 ] )

def solve( part = 1 ):
    pairs = defaultdict( list )
    characterRanking = [ 'A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2' ]
    if part == 2:
        characterRanking = [ 'A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J' ]
    for hand in hands:
        counterHands = defaultdict( int )
        for ch in hand:
            counterHands[ ch ] += 1
        totalLength = len( counterHands )
        maxCount = max( counterHands.values() )

        # Five of a kind
        if maxCount == 5 and totalLength == 1:
            pairs[ 'five-o-a-k' ].append( hand )
            continue

        # Four of a kind
        if maxCount == 4 and totalLength == 2:
            if part == 2 and 'J' in hand:
                # QQQQJ This was 4 of a kind, we can replace J with Q becoming 5 of a kind
                # JJJJA
                pairs[ 'five-o-a-k' ].append( hand )
            else:
                pairs[ 'four-o-a-k' ].append( hand )
            continue

        # Full house
        if maxCount == 3 and totalLength == 2:
            if part == 2 and 'J' in hand:
                # 3JJJ3
                # J333J this is full house with 2 J and 3'3, we can replace both the J with 3 to make it five of a kind
                pairs[ 'five-o-a-k' ].append( hand )
            else:
                pairs[ 'full-house' ].append( hand )
            continue

        # Three of a kind
        if maxCount == 3 and totalLength == 3:
            # TTTJ8 or JJJT8 this can become 4 of a kind
            if part == 2 and 'J' in hand:
                pairs[ 'four-o-a-k' ].append( hand ) 
            else: 
                pairs[ 'three-o-a-k' ].append( hand )
            continue

        # Two Pair
        if maxCount == 2 and totalLength == 3:
            # QJJQ2
            # 23J32 or J323J both are two pairs, if count( j ) == 2 this could become Four of a kind
            # J3322 => 33322 Full House if jCount = 1
            jCount = 0
            for ch in hand:
                if ch == 'J':
                    jCount += 1
            if part == 2 and jCount == 2:
                pairs[ 'four-o-a-k' ].append( hand )
            elif part == 2 and jCount == 1:
                pairs[ 'full-house' ].append( hand )
            else:
                pairs[ 'two-pair' ].append( hand )
            continue

        # One Pair
        if maxCount == 2 and totalLength == 4:
            # AJ3A4 or J53J4
            if part == 2 and 'J' in hand:
                pairs[ 'three-o-a-k' ].append( hand )
            else:
                pairs[ 'one-pair' ].append( hand )
            continue

        # High Card
        if maxCount == 1 and totalLength == 5:
            if part == 2 and 'J' in hand:
                pairs[ 'one-pair' ].append( hand )
            else:
                pairs[ 'high-card' ].append( hand )
            continue

    def sortThem( hands ):
        if len( hands ) == 1:
            return hands # no sorting required
        hasSwapped = True
        while hasSwapped:
            hasSwapped = False
            for i in range( len( hands ) - 1 ):
                hand1 = hands[ i ]
                hand2 = hands[ i + 1 ]
                for ch1, ch2 in zip( hand1, hand2 ):
                    if characterRanking.index( ch1 ) > characterRanking.index( ch2 ):
                        hands[ i ], hands[ i + 1 ] = hands[ i + 1 ], hands[ i ]
                        hasSwapped = True
                        break
                    elif characterRanking.index( ch1 ) < characterRanking.index( ch2 ):
                        break
        return hands[ ::-1 ]
    # Get Ranking
    standings = []
    for key in sorting:
        if key in pairs:
            standings.extend( sortThem( pairs[ key ] ) )

    totalWinnings = 0
    for i in range( len( standings ) ):
        totalWinnings += bidding[ standings[ i ] ] * ( i + 1 )
    return totalWinnings
print( 'Part 1:', solve() ) # 249726565
print( 'Part 2:', solve( 2 ) ) # 251135960