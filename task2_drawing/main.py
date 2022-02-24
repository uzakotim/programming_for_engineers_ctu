#!/usr/bin/python3
# Programming for Engineers - KYR 2021
# CVUT
# Timur Uzakov
import numpy as np

def clear(command, canvas):
    if len(command)!=5:
        print("Wrongly specified clear command, should be: C x1 y1 x2 y2")
        return 
    else:
        x1 = int(command[1])
        y1 = int(command[2])
        x2 = int(command[3])
        y2 = int(command[4])
    canvas_np = np.array(canvas)
    canvas_np[x1:x2+1,y1:y2+1] = 0
    print("Executing Clear")
    return list(canvas_np)

def main():
    # Input parameters
    rows, columns, num_commands = list(map(int,input().split()))
    canvas = [[1]*rows for i in range(columns)]
    commands = []
    for i in range(num_commands):
        commands.append(list(map(str,input().split())))
    output = ''
    for row in range(rows):
        for column in range(columns):
            output+='*'
            if column != columns-1:
                output+=' '
        if row != rows-1:
            output+='\n'

    for i in range(num_commands):
        if (commands[i][0] == 'C'):
            canvas = clear(commands[i],canvas)
        if (commands[i][0] == 'R'):
            print('Executing Rectangle')
        if (commands[i][0] == 'S'):
            print('Executing Substitude')
        if (commands[i][0] == 'P'):
            print('Executing Pyramid')
    for row in canvas:
        print(row)
if __name__ == "__main__":
    main()