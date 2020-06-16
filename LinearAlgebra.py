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
    if magnitude!=0:
        return product/magnitude
    else:
        return product

def normalize(vector1):
    newVector = []
    magnitude = getVectorMagnitude(vector1)
    for x in vector1:
        if magnitude!=0:
            newVector.append(x/magnitude)
        else:
            newVector.append(x)
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
    if isinstance(matrix[0],list):
        for row in matrix:
            for col in row:
                print(str(format(col, '.2f'))+"   ",end="")
            print()
    else:
        for i in matrix:
            print(str(format(i, '.2f'))+"   ",end="")

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

def identity(rows,cols):
    eye = [[] for j in range(rows)]
    index = 0
    for row in eye:
        for i in range(cols):
            if i == index:
                row.append(1)
            else:
                row.append(0)
        index+=1
    return eye

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

def upperTriangularAugment(matrix, y):
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

def getRank(matrix):
    newMatrix = cloneMatrix(matrix)
    matrixWidth = len(matrix[0])
    row=0
    curRow = 0
    col = 0
    rank = 0;

    while col < matrixWidth and curRow< len(newMatrix):
        if newMatrix[curRow][col] != 0:
            rank+=1
            newMatrix[curRow] = scaleElements(newMatrix[curRow],1/(newMatrix[curRow][col]))
            row = curRow+1
            while row < len(newMatrix):
                scalar = newMatrix[row][col]/newMatrix[curRow][col]
                newMatrix[row] = add(scaleElements(newMatrix[curRow],-scalar),newMatrix[row])
                row+=1
            curRow+=1
        col+=1

    return rank

def appendVector(matrix, vector):
    for row in range(len(matrix)):
        matrix[row].append(vector[row])

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

def getVector(matrix, index):
    vector = []
    for row in range(len(matrix)):
        vector.append(matrix[row][index])
    return vector

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

def multiplyMatrices(matrix1, matrix2):
    newMatrix = [[0 for i in range(len(matrix2[0]))] for j in range(len(matrix1))]

    for col in range(len(newMatrix[0])):
        vec = [0 for j in range(len(matrix2))] 
        for row in range(len(matrix2)):
            vec[row] = matrix2[row][col]
        for row in range(len(newMatrix)):
            d = dotProduct(matrix1[row],vec)
            newMatrix[row][col] = d
    return newMatrix

def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        return 'Matrix must be square'
    elif len(matrix) != getRank(matrix):
        return 0
    else:
        newMatrix = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                newMatrix[row][col] = matrix[row][col]
        return determinantHelper(newMatrix,0)

def determinantHelper(matrix, total):
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        sign = 0
        for row in range(len(matrix)):
            newMatrix = cloneMatrix(matrix)
            s = newMatrix[row][0]
            newMatrix.pop(row)
            for col in range(len(newMatrix)):
                newMatrix[col].pop(0)
            if sign==0:
                total+= s * determinantHelper(newMatrix,0)
                sign = 1
            else:
                total+= -s * determinantHelper(newMatrix,0)
                sign = 0
    return total

def ALU(matrix):
    U = cloneMatrix(matrix)
    matrixWidth = len(matrix[0])
    row=0
    curRow = 0
    col = 0
    L = identity(len(matrix),len(matrix[0]))

    while col < matrixWidth and curRow< len(U):
        if U[curRow][col] != 0:
            row = curRow+1
            while row < len(U):
                scalar = U[row][col]/U[curRow][col]
                U[row] = add(scaleElements(U[curRow],-scalar),U[row])
                E = identity(len(matrix),len(matrix[0]))
                E[row][curRow] += -scalar
                L  = multiplyMatrices(E,L)
                row+=1
            curRow+=1
        else:
            row = curRow+1
            while row<len(U):
                if U[row][col] !=0:
                    temp = U[curRow]
                    U[curRow] = U[row]
                    U[row] = temp
                row+=1
            col-=1
        col+=1
    
    return [matrix,inverse(L),U]

def GramSchmidt(matrix):
    orthonormalMatrix = [[] for j in range(len(matrix))]
    index = 0

    for col in range(len(matrix[0])):
        originalVector = getVector(matrix,col)
        newVector = getVector(matrix,col)

        for loc in range(index):
            vecLoc = getVector(orthonormalMatrix, loc)
            projectionLength = getProjectionLength(originalVector,vecLoc)
            normalizedVec = normalize(vecLoc)
            projectionVector = scaleElements(normalizedVec,projectionLength)
            newVector = subtract(newVector,projectionVector)

        v = normalize(newVector)
        appendVector(orthonormalMatrix, v)
        index+=1

    return orthonormalMatrix

def getEigenValues(matrix):
    Qbuilder = identity(len(matrix),len(matrix[0]))
    A = cloneMatrix(matrix)

    for i in range(len(matrix[0])):
        Q = GramSchmidt(A)
        Qbuilder = multiplyMatrices(Qbuilder,Q)
        R = multiplyMatrices(inverse(Q),A)
        A = multiplyMatrices(R,Q)

    eigenvalues = []
    for loc in range(len(A)):
        eigenvalues.append(A[loc][loc])
    return eigenvalues

def getEigenVectors(matrix):
    Qbuilder = identity(len(matrix),len(matrix[0]))
    A = cloneMatrix(matrix)

    for i in range(len(matrix[0])):
        Q = GramSchmidt(A)
        Qbuilder = multiplyMatrices(Qbuilder,Q)
        R = multiplyMatrices(inverse(Q),A)
        A = multiplyMatrices(R,Q)

    return Qbuilder

def eig(matrix):
    Qbuilder = identity(len(matrix),len(matrix[0]))
    A = cloneMatrix(matrix)

    for i in range(len(matrix[0])):
        Q = GramSchmidt(A)
        Qbuilder = multiplyMatrices(Qbuilder,Q)
        R = multiplyMatrices(inverse(Q),A)
        A = multiplyMatrices(R,Q)

    return [A, Qbuilder]

def SVD(matrix):
    AAT = multiplyMatrices(matrix, transpose(matrix))
    eigAAT = eig(AAT)
    U = eigAAT[1]
    ATA = multiplyMatrices(transpose(matrix),matrix)
    eigATA = eig(ATA)
    V = eigATA[1]
    holder = eigATA[0]
    Sigma = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))] 
    for row in range(min(len(Sigma),len(Sigma[0]))):
        Sigma[row][row] = pow(holder[row][row],.5)
    printMatrix(multiplyMatrices(U,multiplyMatrices(Sigma,transpose(V))))
    return [U,Sigma,transpose(V)]
    


matrix1 = [[9,3,9],[3,5,4]]

vector1 = [[2],[4],[5],[6]]

m = SVD(matrix1)
printMatrix(m[0])
printMatrix(m[1])
printMatrix(m[2])
