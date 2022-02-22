# Programming for Engineers - KYR 2021
# CVUT
# Timur Uzakov

import numpy as np
number_of_cells = 2
#Task:
# 1. There are at least two cells in row r to the right of C. The parity of all values in row r to the right of C is the same.
# 2. There are at least two cells in row r to the left of C. The parity of all values in row r to the left of C is the same.
# 3. There are at least two cells in column c above C. The parity of all values in column c above C is the same.
# 4. There are at least two cells in column c below C. The parity of all values in column c below C is the same. 

# Taking input

M, N = input().split()
M = int(M)
N = int(N)
matrix = []
result = []
for x in range(M):
    row = input().split()
    row = [int(x) for x in row]
    matrix.append(row)
     
# Translation into parity form

for i in range(M):
    for j in range(N):
        matrix[i][j] %= 2

result = matrix # temporary matrix

matrix_np = np.array(matrix) #for processing


# Comparing parity of vectors in the 4 directions

for i in range(M):
    for j in range(N):

        if (i>=number_of_cells):
            array_up = matrix_np[:i,j]
        else:
            array_up = np.array([])
        if (i<M-number_of_cells):
            array_down = matrix_np[i+1:,j]
        else:
            array_down = np.array([])        
        
        if (j>=number_of_cells):
            array_left = matrix_np[i,:j]
        else:
            array_left = np.array([])
        
        if (j<N-number_of_cells):
            array_right = matrix_np[i,j+1:]
        else:
            array_right = np.array([])
        
        arrays = [array_up,array_down,array_left,array_right]
        for arr in arrays:
            if ((len(arr)>1) and ((sum(arr)==len(arr)) or (sum(arr)==0))):
                result[i][j] = 1
                break
            else:
                result[i][j] = 0
                
# Print result
for row in result:
    output = str(row)[1:-1]
    output = output.replace(',','')
    output = output.replace('1', 'X')
    output = output.replace('0', '.')
    print(output)