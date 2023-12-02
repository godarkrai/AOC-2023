from collections import defaultdict

with open( 'Day1Input.txt' ) as f:
    input = f.read().splitlines()

def part1():
    # Two Pointer
    total = 0
    for line in input:
        left = 0
        right = len(line) - 1
        firstNumber = ''
        lastNumber = ''
        while left <= right:
            if line[left].isnumeric() and firstNumber == '':
                firstNumber = line[left]
            if line[right].isnumeric() and lastNumber == '':
                lastNumber = line[right]
            if firstNumber != '' and lastNumber != '':
                break
            if firstNumber == '':
                left += 1
            if lastNumber == '':
                right -= 1
        total += int(firstNumber+lastNumber)
    return total

def part2():
    total = 0
    validNumberWords = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7',
        'eight': '8', 'nine': '9'
    }
    validNumbers = [ '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
    for line in input:
        wordsAt = defaultdict(tuple)
        numbersAt = defaultdict(tuple)
        for validWord in validNumberWords:
            minWordAt = line.find( validWord )
            maxWordAt = line.rfind( validWord )
            wordsAt[ validWord ] = (
                minWordAt,
                maxWordAt,
                validNumberWords[ validWord ]
            )
        for validNumber in validNumbers:
            minNumberAt = line.find( validNumber )
            maxNumberAt = line.rfind( validNumber )
            numbersAt[ validNumber ] = (
                minNumberAt,
                maxNumberAt,
                validNumber
            )
        # Get the minimum and maximum index from words
        minIndex = float( 'inf' )
        maxIndex = float( '-inf' )
        firstNumber = ''
        lastNumber = ''
        for (minIdx, maxIdx, number) in wordsAt.values():
            if minIdx != -1 and minIdx < minIndex:
                minIndex = minIdx
                firstNumber = number
            if maxIdx != -1 and maxIdx > maxIndex:
                maxIndex = maxIdx
                lastNumber = number
        for (minIdx, maxIdx, number) in numbersAt.values():
            if minIdx != -1 and minIdx < minIndex:
                minIndex = minIdx
                firstNumber = number
            if maxIdx != -1 and maxIdx > maxIndex:
                maxIndex = maxIdx
                lastNumber = number
        total += int(firstNumber+lastNumber)
    return total
print( "Part 1:", part1() ) # 55130
print( "Part 2:", part2() ) # 54985