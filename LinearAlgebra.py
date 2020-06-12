def dotProduct(vector1, vector2):
    if len(vector1) != len(vector2):
        return 'invalid arguments'
    else:
        total = 0
        for x in range(len(vector1)):
            total+=vector1[x]*vector2[x]
        return total;
        
def crossProduct(vector1, vector2):
    if len(vector1)!=3 or len(vector2)!=3:
        return 'invalid arguments'
    else:
        i = vector1[1]*vector2[2] - vector2[1]*vector1[2]
        j = vector1[0]*vector2[2] - vector2[0]*vector1[2]
        k = vector1[0]*vector2[1] - vector2[0]*vector1[1]
        return [i,-j,k]

def isOrthogonal(vector1,vector2):
    if dotProduct(vector1,vector2)==0:
        return True
    return False

def add(vector1,vector2):
    newVector = []
    if len(vector1) != len(vector2):
        return 'invalid arguments'
    else:
        for x in range(len(vector1)):
            newVector.append(vector1[x]+vector2[x])
        return newVector

def subtract(vector1,vector2):
    newVector = []
    if len(vector1) != len(vector2):
        return 'invalid arguments'
    else:
        for x in range(len(vector1)):
            newVector.append(vector1[x]-vector2[x])
        return newVector

def scaleElements(matrix,scalar):
    if isinstance(matrix[0],list):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                matrix[row][col] = matrix[row][col]*scalar
    else:
        newVector = [0 for j in range(len(matrix))] 
        for x in range(len(matrix)):
            if matrix[x]!=0:
                newVector[x] = matrix[x]*scalar
        return newVector

def transpose(matrix):
    if isinstance(matrix[0],list):
        augmentedMatrix = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))] 
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                augmentedMatrix[y][x] = matrix[x][y]
        return augmentedMatrix
    else:
        augmentedMatrix = [[0] for j in range(len(matrix))] 
        for x in range(len(matrix)):
            augmentedMatrix[x][0] = matrix[x]
        return augmentedMatrix

def printMatrix(matrix):
    for row in matrix:
        for col in row:
            print(str(format(col, '.2f'))+"   ",end="")
        print()

def rowReduce(matrix, y):
    augmentedMatrix = [[0.00 for i in range(len(matrix[0]))] for j in range(len(matrix))]

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            augmentedMatrix[row][col] = matrix[row][col]

    matrixWidth = len(augmentedMatrix[0])
    for rowIndex in range(len(augmentedMatrix)):
        for val in y[rowIndex]:
            augmentedMatrix[rowIndex].append(val)

    row=0
    curRow = 0
    col = 0

    while col < matrixWidth and curRow< len(augmentedMatrix)-1:
        if augmentedMatrix[curRow][col] != 0:
            augmentedMatrix[curRow] = scaleElements(augmentedMatrix[curRow],1/(augmentedMatrix[curRow][col]))
            row = curRow+1
            while row < len(augmentedMatrix):
                scalar = augmentedMatrix[row][col]/augmentedMatrix[curRow][col]
                augmentedMatrix[row] = add(scaleElements(augmentedMatrix[curRow],-scalar),augmentedMatrix[row])
                row+=1
            curRow+=1
        col+=1
    augmentedMatrix[curRow] = scaleElements(augmentedMatrix[curRow],1/(augmentedMatrix[curRow][col]))
    return augmentedMatrix


matrix = [[2,3,5],[5,6,9],[6,8,2]]
v2 = [[1],[5],[2]]
newM = rowReduce(matrix,v2)
printMatrix(newM)

#  [2 3 5 1]
#  [5 6 9 5]
#  [6 8 2 2]


