import copy
possiblePatterns = []

def positionVariants(pattern):
    boards = []
    height = len(pattern)
    width = len(pattern[0])
    for y in range(0,5-height+1):
        for x in range(0,5-width+1):
            board = [['O','O','O','O','O'],
                     ['O','O','O','O','O'],
                     ['O','O','O','O','O'],
                     ['O','O','O','O','O'],
                     ['O','O','O','O','O']]
            for by in range(0,height):
                for bx in range(0,width):
                    board[y+by][x+bx] = pattern[by][bx]
            boards.append(board)
    return boards

def printPattern(pattern):
    for y in range(0,len(pattern)):
        for x in range(0,len(pattern[0])):
            print(pattern[y][x] + ' ', end='')
        print()
    print()

def testBoard(boards,pattern):
    tests = []
    passed = False
    passes = 0
    for y in range(0,5):
        for x in range(0,5):
            if pattern[y][x] == 'X':
                tests.append([y,x])
    for board in boards:
        for test in tests:
            if board[test[0]][test[1]] == 'X':
                passed = True
                passes += 1
                break
        if not(passed):
            break
    return passes == len(boards)

def recursivePattern(board, space, tp, tt):
    y = int(space/5)
    x = space % 5
    if space > 24:
        return
    recursivePattern(copy.deepcopy(board),space+1,tp,tt)
    board[y][x] = 'X'
    if tp + 1 == tt:
        possiblePatterns.append(board)
        return
    recursivePattern(copy.deepcopy(board),space+1,tp+1,tt)

def testPatterns(patterns, boards):
    passedBoards = []
    for pattern in patterns:
        if testBoard(boards, pattern):
            passedBoards.append(pattern)
    return passedBoards

def getPatterns():
    patterns = copy.deepcopy(possiblePatterns)
    possiblePatterns.clear()
    return patterns

pattern = [['O','O','O','O','O'],
           ['O','O','O','O','O'],
           ['O','O','O','O','O'],
           ['O','O','O','O','O'],
           ['O','O','O','O','O']]
hippo = [['X','O','X'],
     ['O','O','O'],
     ['X','O','X']]

hippoBoards = positionVariants(hippo)
printPattern(pattern)
for i in hippoBoards:
    printPattern(i)


