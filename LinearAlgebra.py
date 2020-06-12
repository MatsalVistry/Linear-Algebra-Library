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

def getVectorMagnitude(vector):
    totalSquared = 0
    for x in vector:
        totalSquared+=pow(x,2)
    return pow(totalSquared,.5)

def getProjectionLength(vector1,vector2):
    product = dotProduct(vector1,vector2)
    magnitude = getVectorMagnitude(vector2)
    return product/magnitude

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
        newMatrix = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))] 
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                newMatrix[y][x] = matrix[x][y]
        return newMatrix
    else:
        newMatrix = [[0] for j in range(len(matrix))] 
        for x in range(len(matrix)):
            newMatrix[x][0] = matrix[x]
        return newMatrix

def printMatrix(matrix):
    for row in matrix:
        for col in row:
            print(str(format(col, '.2f'))+"   ",end="")
        print()

def getAugmentedMatrix(matrix, y):
    augmentedMatrix = [[0.00 for i in range(len(matrix[0]))] for j in range(len(matrix))]

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            augmentedMatrix[row][col] = matrix[row][col]

    matrixWidth = len(augmentedMatrix[0])
    for rowIndex in range(len(augmentedMatrix)):
        for val in y[rowIndex]:
            augmentedMatrix[rowIndex].append(val)
    return augmentedMatrix

def cloneMatrix(matrix):
    cloneMatrix = [[0.00 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            cloneMatrix[row][col] = matrix[row][col]
    return cloneMatrix

def invertedAugmentMatrix(matrix):
    invertedAugmentMatrix = [[0.00 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            invertedAugmentMatrix[row][col] = matrix[row][col]

    index = 0
    matrixWidth = len(invertedAugmentMatrix[0])
    for row in invertedAugmentMatrix:
        for i in range(matrixWidth):
            if i == index:
                row.append(1)
            else:
                row.append(0)
        index+=1
    return invertedAugmentMatrix

def rowReduce(matrix, y):
    augmentedMatrix = getAugmentedMatrix(matrix,y)
    matrixWidth = len(matrix[0])
    row=0
    curRow = 0
    col = 0

    while col < matrixWidth and curRow< len(augmentedMatrix):
        if augmentedMatrix[curRow][col] != 0:
            augmentedMatrix[curRow] = scaleElements(augmentedMatrix[curRow],1/(augmentedMatrix[curRow][col]))
            row = curRow+1
            while row < len(augmentedMatrix):
                scalar = augmentedMatrix[row][col]/augmentedMatrix[curRow][col]
                augmentedMatrix[row] = add(scaleElements(augmentedMatrix[curRow],-scalar),augmentedMatrix[row])
                row+=1
            curRow+=1
        else:
            row = curRow+1
            while row<len(augmentedMatrix):
                if augmentedMatrix[row][col] !=0:
                    temp = augmentedMatrix[curRow]
                    augmentedMatrix[curRow] = augmentedMatrix[row]
                    augmentedMatrix[row] = temp
                row+=1
            col-=1
        col+=1

    return augmentedMatrix

def getRank(matrix, y):
    augmentedMatrix = getAugmentedMatrix(matrix,y)
    matrixWidth = len(matrix[0])
    row=0
    curRow = 0
    col = 0
    rank = 0;

    while col < matrixWidth and curRow< len(augmentedMatrix):
        if augmentedMatrix[curRow][col] != 0:
            rank+=1
            augmentedMatrix[curRow] = scaleElements(augmentedMatrix[curRow],1/(augmentedMatrix[curRow][col]))
            row = curRow+1
            while row < len(augmentedMatrix):
                scalar = augmentedMatrix[row][col]/augmentedMatrix[curRow][col]
                augmentedMatrix[row] = add(scaleElements(augmentedMatrix[curRow],-scalar),augmentedMatrix[row])
                row+=1
            curRow+=1
        col+=1

    return rank

def rowReducedEchelonForm(matrix, y):
    augmentedMatrix = getAugmentedMatrix(matrix,y)
    matrixWidth = len(matrix[0])
    row=0
    curRow = 0
    col = 0
    lastPivRow = 0
    lastPivCol = 0

    while col < matrixWidth and curRow< len(augmentedMatrix):
        if augmentedMatrix[curRow][col] != 0:
            lastPivRow=curRow
            lastPivCol=col
            augmentedMatrix[curRow] = scaleElements(augmentedMatrix[curRow],1/(augmentedMatrix[curRow][col]))
            row = curRow+1
            while row < len(augmentedMatrix):
                scalar = augmentedMatrix[row][col]/augmentedMatrix[curRow][col]
                augmentedMatrix[row] = add(scaleElements(augmentedMatrix[curRow],-scalar),augmentedMatrix[row])
                row+=1
            curRow+=1
        else:
            row = curRow+1
            while row<len(augmentedMatrix):
                if augmentedMatrix[row][col] !=0:
                    temp = augmentedMatrix[curRow]
                    augmentedMatrix[curRow] = augmentedMatrix[row]
                    augmentedMatrix[row] = temp
                    col-=1
                    break
                row+=1     
        col+=1

    col = lastPivCol;
    curRow = lastPivRow;

    while col!=0:
        if augmentedMatrix[curRow][col]!=0:
            row = curRow-1
            while row!=-1:
                scalar = augmentedMatrix[row][col]/augmentedMatrix[curRow][col]
                augmentedMatrix[row] = add(scaleElements(augmentedMatrix[curRow],-scalar),augmentedMatrix[row])
                row-=1
            curRow-=1
        col-=1

    return augmentedMatrix

def inverse(matrix):
    if len(matrix) != len(matrix[0]):
        return 'Matrix is non invertible'
    else:
        invertedMatrix = invertedAugmentMatrix(matrix)
        matrixWidth = len(matrix[0])
        row=0
        curRow = 0
        col = 0
        lastPivRow = 0
        lastPivCol = 0

        while col < matrixWidth and curRow< len(invertedMatrix):
            if invertedMatrix[curRow][col] != 0:
                lastPivRow=curRow
                lastPivCol=col
                invertedMatrix[curRow] = scaleElements(invertedMatrix[curRow],1/(invertedMatrix[curRow][col]))
                row = curRow+1
                while row < len(invertedMatrix):
                    scalar = invertedMatrix[row][col]/invertedMatrix[curRow][col]
                    invertedMatrix[row] = add(scaleElements(invertedMatrix[curRow],-scalar),invertedMatrix[row])
                    row+=1
                curRow+=1
            else:
                row = curRow+1
                while row<len(invertedMatrix):
                    if invertedMatrix[row][col] !=0:
                        temp = invertedMatrix[curRow]
                        invertedMatrix[curRow] = invertedMatrix[row]
                        invertedMatrix[row] = temp
                        col-=1
                        break
                    row+=1     
            col+=1

        col = lastPivCol;
        curRow = lastPivRow;

        while col!=0:
            if invertedMatrix[curRow][col]!=0:
                row = curRow-1
                while row!=-1:
                    scalar = invertedMatrix[row][col]/invertedMatrix[curRow][col]
                    invertedMatrix[row] = add(scaleElements(invertedMatrix[curRow],-scalar),invertedMatrix[row])
                    row-=1
                curRow-=1
            col-=1

    for row in range(len(invertedMatrix)):
        invertedMatrix[row] = invertedMatrix[row][matrixWidth:]
    return invertedMatrix



matrix = [[3,4,5,7],[3,1,6,7],[5,2,8,6],[3,4,6,7]]

v2 = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
vec = [1,5,10]
newM = inverse(matrix)
rank = getRank(matrix,v2)

print(rank)
printMatrix(newM)

