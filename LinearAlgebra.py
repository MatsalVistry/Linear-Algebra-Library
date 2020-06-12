def dotProduct(vector1, vector2):
    if(len(vector1) != len(vector2)):
        return -1
    else:
        total = 0
        for x in range(len(vector1)):
            total+=vector1[x]*vector2[x]
        return total;
        


v1 = [1,2,3]
v2 = [3,4,5]
print(dotProduct(v1,v2))