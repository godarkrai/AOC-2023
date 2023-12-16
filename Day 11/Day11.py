from collections import defaultdict
from copy import deepcopy

with open('Day11Input.txt') as f:
    line = f.read().splitlines()

grid = []

currentGalaxy = 1
for line in line:
    line = [*line]
    grid.append(line)

R = len(grid)
C = len(grid[0])
countRow = defaultdict(int)
countCol = defaultdict(int)
hashLocations = []
for row in range(R):
    for col in range(C):
        countRow[row] += 0 if grid[row][col] == '.' else 1
        countCol[col] += 0 if grid[row][col] == '.' else 1
        if grid[row][col] == '#':
            hashLocations.append((row, col))


# Instead of expansion, just add the penalty due to expansion in the manhattan distance
def solve(expansion):
    totalDistance = 0
    visited = set()
    for i in range(len(hashLocations)):
        for j in range(len(hashLocations)):
            if i == j:
                continue
            if (i, j) in visited or (j, i) in visited:
                continue
            visited.add((i, j))
            firstX = hashLocations[i][0]
            secondX = hashLocations[j][0]
            firstY = hashLocations[i][1]
            secondY = hashLocations[j][1]
            distance = abs(firstX - secondX) + abs(firstY - secondY)
            for row in range(min(firstX, secondX) + 1, max(firstX, secondX)):
                if countRow[row] == 0:
                    distance += expansion - 1
            for col in range(min(firstY, secondY) + 1, max(firstY, secondY)):
                if countCol[col] == 0:
                    distance += expansion - 1
            # If there is a column added before the destination, add the total expansion amount - 1
            totalDistance += distance
    return totalDistance


print('Part 1:', solve(2))  # 9233514
print('Part 2:', solve(1000000))  # 363293506944
