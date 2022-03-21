#!/usr/bin/python3
# Programming for Engineers - KYR 2021
# Graphical Editor
# CVUT
# Timur Uzakov
import numpy as np


def main():
    result = []
    x = input("Please, enter size:")
    for i in range(0,int(x)):
        row =[]
        for j in range(0,int(x)):
            row.append(" ")
        result.append(row)

    for i in range(0,int(x)):
        for j in range(int(x)):
            if (j ==0) or (i==0) or (i ==j) or (i == int(x)-1) or (j == int(x)-1) or (i == int(x)-j-1):
                result[i][j] = "#"
        

    output =''
    for i,row in enumerate(result):
        for j,element in enumerate(row):
            output+= result[i][j]
            if (j != int(x)-1):
                output+=' '
        if (i != int(x)-1):
            output+='\n'
    print(output)

if __name__ == "__main__":
    main()