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

''' 
Output:

1. Text:
lorem ipsum dolor sit amet, consetetur sadipscing elitr

2. Text:
duis aute irure dolor in velit esse cillum
Matrix:
[[ 0.  1.  2. ... 40. 41. 42.]
 [ 1.  1.  2. ... 39. 40. 41.]
 [ 2.  2.  2. ... 38. 39. 40.]
 ...
 [53. 52. 51. ... 39. 39. 40.]
 [54. 53. 52. ... 40. 40. 40.]
 [55. 54. 53. ... 41. 41. 41.]]

Levenshtein distance: 41


Matrix position:
[55 42] [54 42] [53 41] [52 40] [51 39] [50 39] [49 39] [48 39] [47 38] [46 37] [45 36] [44 36] [43 36] [42 36] [41 36] [40 36] 
[39 36] [38 35] [37 35] [36 35] [35 35] [34 35] [33 35] [32 34] [31 33] [30 33] [29 32] [28 31] [27 30] [26 30] [25 29] [25 28] 
[25 27] [24 26] [23 26] [22 25] [21 24] [20 23] [19 22] [18 22] [17 21] [16 20] [15 19] [14 18] [13 17] [12 16] [11 15] [11 14] 
[10 13] [9 12] [8 12] [7 11] [6 10] [5 9] [4 9] [3 8] [3 7] [3 6] [3 5] [3 4] [3 3] [2 2] [1 1]

Strings with edit distance:
lor-----em ipsum- dolor sit ame--t, consetetur sadipscing elitr
duis aute- ir-ure dolor -in v-elit- es-se----- ------cil---lum-

'''
