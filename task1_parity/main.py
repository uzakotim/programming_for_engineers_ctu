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
    number_of_cells = 2
    output = ''

    # Storing matrix and conversion to sparity form 
    matrix = [list(map(parity,input().split())) for i in range(rows)]
    matrix_np = np.array(matrix) #for processing

    # Comparing parity of vectors in the 4 directions
    
    for i in range(rows):
        for j in range(columns):
            if (i>=number_of_cells):
                array_up = matrix_np[:i,j]
                if (sum(array_up) == len(array_up)) or (sum(array_up) ==0):
                    
                    output += 'X'

                    if (j==(columns-1)):
                        output+='\n'
                    else:
                        output+=' '
                    continue

            if (i<rows-number_of_cells):
                array_down = matrix_np[i+1:,j]
                if (sum(array_down) == len(array_down)) or (sum(array_down) ==0):
                    output += 'X'
                    if (j==(columns-1)):
                        output+='\n'
                    else:
                        output+=' '
                    continue


            if (j>=number_of_cells):
                array_left = matrix_np[i,:j]
                if (sum(array_left) == len(array_left)) or (sum(array_left) ==0):
                    output += 'X'
                    if (j==(columns-1)):
                        output+='\n'
                    else:
                        output+=' '
                    continue


            
            if (j<columns-number_of_cells):
                array_right = matrix_np[i,j+1:]
                if (sum(array_right) == len(array_right)) or (sum(array_right) ==0):
                    output += 'X'
                    if (j==(columns-1)):
                        output+='\n'
                    else:
                        output+=' '
                    continue

            output += '.'
            if (j==(columns-1)):
                output+='\n'
            else:
                output+=' '
            continue
    output = output[:-1]
    print(output)

if __name__ == "__main__":
    main()

