with open( 'Day1Input.txt' ) as f:
    input = f.read().splitlines()

def part1():
    total = 0
    for line in input:
        numbers = []
        for ch in line:
            if ch.isnumeric():
                numbers.append(ch)
        if len(numbers) == 1:
            curTotal = numbers[0] * 2
        else:
            curTotal = numbers[0] + numbers[-1]
        total += int(curTotal)
    return total

def part2():
    res = []
    validNumberWords = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7',
        'eight': '8', 'nine': '9'
    }
    validNumbers = [ '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
    for line in input:
        minWordIndex = float( 'inf' )
        maxWordIndex = float( '-inf' )
        minNumberIndex = float( 'inf' )
        maxNumberIndex = float( '-inf' )
        minWord = ''
        minNumber = ''
        maxWord = ''
        maxNumber = ''
        for validWord in validNumberWords:
            minWordAt = line.find( validWord )
            maxWordAt = line.rfind( validWord )
            if minWordAt != -1 and minWordAt < minWordIndex:
                minWordIndex = minWordAt
                minWord = validWord
            if maxWordAt != -1 and maxWordAt > maxWordIndex:
                maxWordIndex = maxWordAt
                maxWord = validWord
        for validNumber in validNumbers:
            minNumberAt = line.find( validNumber )
            maxNumberAt = line.rfind( validNumber )
            if minNumberAt != -1 and minNumberAt < minNumberIndex:
                minNumberIndex = minNumberAt
                minNumber = validNumber
            if maxNumberAt > maxNumberIndex:
                maxNumberIndex = maxNumberAt
                maxNumber = validNumber
        if minWordIndex < minNumberIndex:
            firstLetter = validNumberWords[ minWord ]
        else:
            firstLetter = minNumber
        
        if maxWordIndex > maxNumberIndex:
            lastLetter = validNumberWords[ maxWord ]
        else:
            lastLetter = maxNumber
        res.append(firstLetter+lastLetter)
    return sum( list( map(int, res) ) )
print( "Part 1:", part1() ) # 55130
print( "Part 2:", part2() ) # 54985