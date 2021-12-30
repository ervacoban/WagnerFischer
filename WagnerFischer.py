import numpy as np

def wagnerFischer(Q, R):
    matrix = np.zeros((len(Q) + 1, len(R) + 1)) 
    for i in range(len(Q) + 1):
        matrix[i, 0] = i
    
    for j in range(len(R) + 1):
        matrix[0, j] = j

    for i in range(1, len(Q) + 1):
        for j in range(1, len(R) + 1):
            x = matrix[i - 1, j] + 1
            y = matrix[i, j - 1] + 1 
            z = matrix[i - 1, j - 1] 
            if Q[i - 1] != R[j - 1]:
                z += 1 
            
            matrix[i, j] = min(x, y, z)
    
    print("Matrix:\n" + str(matrix)) 
    return int((matrix[len(Q), len(R)])), matrix # returns levenshtein distance and matrix table

def wagnerFischerPrint(Q, R, matrix):
    i = len(Q)
    j = len(R)
    qStack = [] 
    rStack = []
    print("\nMatrix position:")
    while i != 0 or j != 0:
        print("[" + str(i) + " " + str(j) + "]", end= " ")
        if i > 0 and matrix[i - 1, j] < matrix[i, j]: 
            qStack.append(Q[i - 1])
            rStack.append('-') 
            i -= 1
        
        elif j > 0 and matrix[i, j - 1] < matrix[i, j]: 
            qStack.append('-')  
            rStack.append(R[j - 1])
            j -= 1
        
        else:
            qStack.append(Q[i - 1]) 
            rStack.append(R[j - 1])
            i -= 1
            j -= 1

    return qStack, rStack

text1 = "lorem ipsum dolor sit amet, consetetur sadipscing elitr"
text2 = "duis aute irure dolor in velit esse cillum"

print("1. Text:\n" + text1)
print("\n2. Text:\n" + text2)

levenshteinDistance, matrix = wagnerFischer(text1, text2)
print("\nLevenshtein distance: " + str(levenshteinDistance) + "\n")

qStack, rStack = wagnerFischerPrint(text1, text2, matrix)
qString = ''.join(qStack) # add stack elements to string
rString = ''.join(rStack)
qString = qString[::-1] # reverse the string
rString = rString[::-1]
print("\n\nStrings with edit distance:\n" + qString + "\n" + rString)