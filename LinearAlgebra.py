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

v1 = [0,0,0]
v2 = [1,1,1]
print(isOrthogonal(v1,v2))