#!/usr/bin/python3
# Programming for Engineers - KYR 2021
# CVUT
# Timur Uzakov

import numpy as np

def parity(n):
    return int(n)%2

def main():
    # Input parameters
    rows, columns = list(map(int,input().split()))
    matrix = []
    output = ''

    # Storing matrix and conversion to sparity form 
    matrix = [list(map(parity,input().split())) for i in range(rows)]
    matrix_np = np.array(matrix)

    right = [ [0]*columns for i in range(rows)]
    # right
    for i in range(rows):
        stored = None
        for j in range(columns): 
            reversed_index = columns-1-j
            if stored == -1:
                right[i][reversed_index] = 0
                continue
            if j==2:
                if matrix[i][reversed_index+1] == matrix[i][reversed_index+2] and matrix[i][reversed_index+1] == 0:
                    stored = 0
                    right[i][reversed_index] = 1 # even
                if matrix[i][reversed_index+1] == matrix[i][reversed_index+2] and matrix[i][reversed_index+1] == 1:
                    stored = 1
                    right[i][reversed_index] = 1 #odd
                elif matrix[i][reversed_index+1] != matrix[i][reversed_index+2]:
                    stored = -1
                    right[i][reversed_index] = 0 #mixed

            if j>=3:
                if matrix[i][reversed_index+1] == stored and stored == 0:
                    stored = 0
                    right[i][reversed_index] = 1 #even
                elif matrix[i][reversed_index+1] == stored and stored == 1:
                    stored = 1
                    right[i][reversed_index] = 1 #odd
                elif matrix[i][reversed_index+1] != stored:
                    stored = -1
                    right[i][reversed_index] = 0 #mixed

    left = [ [0]*columns for i in range(rows)]
    # left      
    for i in range(rows):
        stored = None
        for j in range(columns): 
            reversed_index = j
            if stored == -1:
                left[i][reversed_index]=0
                continue
            if j==2:
                if matrix[i][reversed_index-1] == matrix[i][reversed_index-2] and matrix[i][reversed_index-1] == 0:
                    stored = 0
                    left[i][reversed_index] = 1 #even
                if matrix[i][reversed_index-1] == matrix[i][reversed_index-2] and matrix[i][reversed_index-1] == 1:
                    stored = 1
                    left[i][reversed_index] = 1 #odd
                elif matrix[i][reversed_index-1] != matrix[i][reversed_index-2]:
                    stored = -1
                    left[i][reversed_index] = 0 #mixed

            if j>=3:
                if matrix[i][reversed_index-1] == stored and stored == 0:
                    stored = 0
                    left[i][reversed_index] = 1 #even
                elif matrix[i][reversed_index-1] == stored and stored == 1:
                    stored = 1
                    left[i][reversed_index] = 1 #odd
                elif matrix[i][reversed_index-1] != stored:
                    stored = -1
                    left[i][reversed_index] = 0 #mixed
                   
    up = [ [0]*columns for i in range(rows)]
    # up
    for j in range(columns):
        stored = None
        for i in range(rows): 
            reversed_index = i
            if stored == -1:
                up[reversed_index][j] = 0
                continue
            if i==2:
                if matrix[reversed_index-1][j] == matrix[reversed_index-2][j] and matrix[reversed_index-1][j] == 0:
                    stored = 0
                    up[reversed_index][j] = 1 #even
                if matrix[reversed_index-1][j] == matrix[reversed_index-2][j] and matrix[reversed_index-1][j] == 1:
                    stored = 1
                    up[reversed_index][j] = 1 #odd
                elif matrix[reversed_index-1][j] != matrix[reversed_index-2][j]:
                    stored = -1
                    up[reversed_index][j] = 0 #mixed 

            if i>=3:
                if matrix[reversed_index-1][j] == stored and stored == 0:
                    stored = 0
                    up[reversed_index][j] = 1 #even
                elif matrix[reversed_index-1][j] == stored and stored == 1:
                    stored = 1
                    up[reversed_index][j] = 1 #odd
                elif matrix[reversed_index-1][j] != stored:
                    stored = -1
                    up[reversed_index][j] = 0 #mixed
 
    down = [ [0]*columns for i in range(rows)]
    # down
    for j in range(columns):
        stored = None
        for i in range(rows): 
            reversed_index = rows-1-i
            if stored == -1:
                down[reversed_index][j] = 0
                continue
            if i==2:
                if matrix[reversed_index+1][j] == matrix[reversed_index+2][j] and matrix[reversed_index+1][j] == 0:
                    stored = 0
                    down[reversed_index][j] = 1 #even
                if matrix[reversed_index+1][j] == matrix[reversed_index+2][j] and matrix[reversed_index+1][j] == 1:
                    stored = 1
                    down[reversed_index][j] = 1 #odd
                elif matrix[reversed_index+1][j] != matrix[reversed_index+2][j]:
                    stored = -1
                    down[reversed_index][j] = 0 #mixed

            if i>=3:
                if matrix[reversed_index+1][j] == stored and stored == 0:
                    stored = 0
                    down[reversed_index][j] = 1 #even
                elif matrix[reversed_index+1][j] == stored and stored == 1:
                    stored = 1
                    down[reversed_index][j] = 1 #odd
                elif matrix[reversed_index+1][j] != stored:
                    stored = -1
                    down[reversed_index][j] = 0 #mixed

    left_np = np.array(left)
    right_np = np.array(right)
    up_np = np.array(up)
    down_np = np.array(down)

    result = left_np+right_np+up_np+down_np

    for i in range(rows):
        for j in range(columns):
            if result[i,j] >0:
                output+='X'
            else:
                output+='.'
            if j!=(columns-1):
                output+=' '
        if (i!=(rows-1)):
            output+='\n'

    print(output)    

if __name__ == "__main__":
    main()

