import itertools
import re

horizontal = [
    [7,3,1,1,7],
    [1,1,2,2,1,1],
    [1,3,1,3,1,1,3,1],
    [1,3,1,1,6,1,3,1],
    [1,3,1,5,2,1,3,1],
    [1,1,2,1,1],
    [7,1,1,1,1,1,7],
    [3,3],
    [1,2,3,1,1,3,1,1,2],
    [1,1,3,2,1,1],
    [4,1,4,2,1,2],
    [1,1,1,1,4,1,3],
    [2,1,1,1,2,5],
    [3,2,2,6,3,1],
    [1,9,1,1,2,1],
    [2,1,2,2,3,1],
    [3,1,1,1,1,5,1],
    [1,2,2,5],
    [7,1,2,1,1,3],
    [1,1,2,1,2,2,1],
    [1,3,1,4,5,1],
    [1,3,1,3,10,2],
    [1,3,1,1,6,6],
    [1,1,2,1,1,2],
    [7,2,1,2,5]
]
vertical = [
    [7,2,1,1,7],
    [1,1,2,2,1,1],
    [1,3,1,3,1,3,1,3,1],
    [1,3,1,1,5,1,3,1],
    [1,3,1,1,4,1,3,1],
    [1,1,1,2,1,1],
    [7,1,1,1,1,1,7],
    [1,1,3],
    [2,1,2,1,8,2,1],
    [2,2,1,2,1,1,1,2],
    [1,7,3,2,1],
    [1,2,3,1,1,1,1,1],
    [4,1,1,2,6],
    [3,3,1,1,1,3,1],
    [1,2,5,2,2],
    [2,2,1,1,1,1,1,2,1],
    [1,3,3,2,1,8,1],
    [6,2,1],
    [7,1,4,1,1,3],
    [1,1,1,1,4],
    [1,3,1,3,7,1],
    [1,3,1,1,1,2,1,1,4],
    [1,3,1,4,3,3],
    [1,1,2,2,2,6,1],
    [7,1,3,2,1,1]
]
grid = [
    # 1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25
    ["?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","X","X","?","?","?","?","?","?","?","X","X","?","?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","X","X","?","?","X","?","?","?","X","X","?","?","X","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","X","?","?","?","?","X","?","?","?","?","X","?","?","?","X","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","X","X","?","?","?","?","X","X","?","?","?","?","X","?","?","?","?","X","X","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?"],
    ["?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?"],
]
oRegex = re.compile(r"^\?O+$")
xRegex = re.compile(r"^\?X+$")

def genRowCombinations(row):
    rowCombinations = []
    rowSum = sum(row)
    rowLength = len(row)
    spaces = 25 - rowSum
    gaps = rowLength - 1
    spaceGapDiff = spaces - gaps
    spaceCombinations = [x for x in itertools.product(range(1, spaceGapDiff+2), repeat=gaps) if sum(x) == spaces]
    for spaceCombonation in spaceCombinations:
        newRow = ""
        for x in range(0, rowLength):
            newRow += "X" * row[x]
            if x < rowLength - 1:
                newRow += "O" * spaceCombonation[x]
        rowCombinations.append(newRow)
    if spaceGapDiff == 0:
        return rowCombinations
    gaps += 1;
    spaceGapDiff = spaces - gaps
    spaceCombinations = [y for y in itertools.product(range(1, spaceGapDiff+2), repeat=gaps) if sum(y) == spaces]
    for spaceCombonation in spaceCombinations:
        newRow = ""
        for x in range(0, rowLength):
            newRow += "X" * row[x]
            if x < rowLength - 1:
                newRow += "O" * spaceCombonation[x]
        newRowGapStart = newRow + ("O" * spaceCombonation[gaps - 1])
        rowCombinations.append(newRowGapStart)
        newRowGapEnd = ("O" * spaceCombonation[gaps - 1]) + newRow
        rowCombinations.append(newRowGapEnd)
    if spaceGapDiff == 1:
        return rowCombinations
    gaps += 1;
    spaceGapDiff = spaces - gaps
    spaceCombinations = [z for z in itertools.product(range(1, spaceGapDiff+2), repeat=gaps) if sum(z) == spaces]
    for spaceCombonation in spaceCombinations:
        newRow = ""
        for x in range(0, rowLength):
            newRow += "O" * spaceCombonation[x]
            newRow += "X" * row[x]
        newRow += "O" * spaceCombonation[gaps - 1]
        rowCombinations.append(newRow)
    return rowCombinations

def compareRows(rows, i):
    newRow = list(grid[i])
    for row in rows:
        skip = False
        for x in range(25):
            if grid[i][x] != "?" and grid[i][x] != row[x]:
                skip = True
                break
        if not skip:
            for x in range(25):
                newRow[x] += row[x]
    for valGroupIndex in range(25):
        if oRegex.match(newRow[valGroupIndex]):
            grid[i][valGroupIndex] = "O"
        elif xRegex.match(newRow[valGroupIndex]):
            grid[i][valGroupIndex] = "X"

def compareCols(cols, i):
    newCol = list([row[i] for row in grid])
    for col in cols:
        skip = False
        for x in range(25):
            if grid[x][i] != "?" and grid[x][i] != col[x]:
                skip = True
                break
        if not skip:
            for x in range(25):
                newCol[x] += col[x]
    for valGroupIndex in range(25):
        if oRegex.match(newCol[valGroupIndex]):
            grid[valGroupIndex][i] = "O"
        elif xRegex.match(newCol[valGroupIndex]):
            grid[valGroupIndex][i] = "X"

def passThrough():
    for x in range(25):
        compareRows(genRowDict[x], x)
    for y in range(25):
        compareCols(genColDict[y], y)
    print grid

genRowDict = []
genColDict = []
for row in horizontal:
    genRows = genRowCombinations(row)
    genRowDict.append(genRows)

for column in vertical:
    genCols = genRowCombinations(column)
    genColDict.append(genCols)

passThrough()

#TODO Check For solution, run passthrough on loop until solved.
