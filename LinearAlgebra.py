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
        for x in range(len(matrix)):
            matrix[x] = matrix[x]*scalar

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

matrix = [[2,3,4],[5,6,7]]
v2 = [1,5,8]
print(transpose(matrix))   


