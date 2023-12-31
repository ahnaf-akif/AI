import matplotlib.pyplot as plt
import random
import numpy as np

# 0 -> clean
# 1 -> wall
# 2 -> dirt

matrix =np.array([
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0,1.0, 1.0],       #6x6 matrix
    [1.0, 0.1, 0.1, 0.1, 0.4, 0.4,0.5, 1.0],
    [1.0, 0.1, 0.1, 0.1, 0.6, 0.4,0.4, 1.0], 
    [1.0, 0.1, 0.4, 0.1, 0.1, 0.1,0.1, 1.0], 
    [1.0, 0.4, 0.6, 0.4, 0.1, 0.1,0.1, 1.0],
    [1.0, 0.1, 0.4, 0.1, 0.1, 0.1,0.1, 1.0],
    [1.0, 0.1, 0.4, 0.1, 0.1, 0.1,0.1, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0,1.0, 1.0]
])
# Create environment, so each run will result in different environments.


def createWorld(m):
    for row in range(1, 7):
        for col in range(1, 7):
            if (random.random() < m[row][col]):
                m[row][col] = 2
            else:
                m[row][col] = 0
    # renderMatrix(matrix)

# Actions = up (0), down (1), left (2), right (3), clean(4), idle (6)


def findNextAction(x, y):
    if x == 1 and y == 1:  # top left corner
        action = random.choice([1, 3, 6])
    elif x == 1 and y == 6:  # top right corner
        action = random.choice([1, 2, 6])
    elif x == 6 and y == 1:  # bottom left corner
        action = random.choice([0, 3, 6])
    elif x == 6 and y == 6:  # bottom right corner
        action = random.choice([0, 2, 6])
    elif x == 1:
        action = random.choice([1, 2, 3, 6])
    elif x == 6:
        action = random.choice([0, 2, 3, 6])
    elif y == 1:
        action = random.choice([0, 1, 3, 6])
    elif y == 6:
        action = random.choice([0, 1, 2, 6])
    else:
        action = random.choice([0, 1, 2, 3, 6])
    return action


def renderMatrix(matrix, x, y, utility, timeElapsed):
    plt.text(0, 0, "Time Elapsed:%d; Utility: %.1f" % (timeElapsed, utility))
    plt.imshow(matrix, 'pink')
    plt.show(block=False)
    plt.plot(y, x, 'r:', linewidth=1)
    plt.plot(y[len(y)-1], x[len(x)-1], '*r', 'Robot field', 6)
    plt.pause(0.5)
    plt.clf()
# decides which action will be done
# Actions = up (0), down (1), left (2), right (3), clean(4)


def simpleAgentRobot(x, y):
    if (matrix[x][y] == 2):  # if it's dirty, return the clean action
        return 4
    return findNextAction(x, y)


# def checkDirtSpots(matrix):
#     x = len(matrix)
#     totalones = 2*x+(x-2)*2
#     sum = np.sum(matrix)-totalones*2
#     return (sum)


def main():
    createWorld(matrix)
    print("Environment (beginning)\r\n")
    colCount = 0
    for row in matrix:
        for col in row:
            if (len(row)-1 == colCount):
                colCount = 0
                print(f'{col}\n')
                break
            else:
                print(f'{str(col)}\t', end=" ")
                colCount = colCount+1
    #the robot always starts from point(1,1)
    currLine = 1
    currCol = 1
    Lines = []
    Cols = []
    Lines.append(currLine)
    Cols.append(currCol)
    utility = 0
    timeElapsed = 0
    renderMatrix(matrix, Lines, Cols, utility, timeElapsed)
    #totalDirt = checkDirtSpots(matrix)
    while True:
        if 2 not in matrix:
            print("end")
            break
        action = simpleAgentRobot(currLine, currCol)
        if (action == 0):  # go up
            print("up")
            currLine = currLine - 1  # remove 1 line
            utility = utility-1
        elif (action == 1):  # go down
            print("down")
            currLine = currLine + 1
            utility = utility-1
        elif (action == 2):  # go left
            print("left")
            currCol = currCol - 1
            utility = utility-1
        elif (action == 3):  # go right
            print("right")
            currCol = currCol + 1
            utility = utility-1
        elif (action == 4):  # clean
            print("clean")
            matrix[currLine][currCol] = 0
            utility = utility+10
        elif (action == 6):  # idle
            print("idle")
            utility = utility+0
        Lines.append(currLine)
        Cols.append(currCol)
        timeElapsed = timeElapsed+1
        renderMatrix(matrix, Lines, Cols, utility, timeElapsed)
    print("Environment (ending): %f\r\n" % utility)

    colCount = 0
    for row in matrix:
        for col in row:
            if (len(row)-1 == colCount):
                colCount = 0
                print(f'{col}\n')
                break
            else:
                print(f'{str(col)}\t', end=" ")
                colCount = colCount+1

if __name__ == "__main__":
    main()
