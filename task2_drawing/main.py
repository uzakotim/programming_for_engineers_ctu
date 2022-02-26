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
    canvas_np[x1:x2+1,y1:y2+1] = -1
    print("Executing Clear")
    return list(canvas_np)

def rectangle(command, canvas):
    if len(command)!=6:
        print("Wrongly specified clear command, should be: R x1 y1 x2 y2 char")
        return 
    else:
        x1 = int(command[1])
        y1 = int(command[2])
        x2 = int(command[3])
        y2 = int(command[4])
        character = ord(command[5])

    canvas_np = np.array(canvas)
    canvas_np[x1:x2+1,y1:y2+1] = character
    print("Executing Rectangle")
    return list(canvas_np)


def substitute(command, canvas):
    if len(command)!=7:
        print("Wrongly specified clear command, should be: S x1 y1 x2 y2 char char")
        return 
    else:
        x1 = int(command[1])
        y1 = int(command[2])
        x2 = int(command[3])
        y2 = int(command[4])
        character_old = ord(command[5])
        character_new = ord(command[6])
    
    canvas_np = np.array(canvas)
    canvas_np[x1:x2+1,y1:y2+1][canvas_np[x1:x2+1,y1:y2+1] == character_old] = character_new

    print("Executing Substitute")
    return list(canvas_np)

def pyramid(command, canvas,columns,rows):
    if len(command)!=5:
        print("Wrongly specified clear command, should be: P y1 x1 x2 char")
        return 
    else:
        y1 = int(command[1])
        x1 = int(command[2])
        x2 = int(command[3])
        character = ord(command[4])
    
    canvas_np = np.array(canvas)
    i = 0
    while (x1+i<=x2+1-i):
        if (y1-i)<rows and (y1-i>0):
            canvas_np[y1-i,x1+i:x2+1-i] = character
        i+=1
    print("Executing Pyramid")
    return list(canvas_np)

def main():
    # Input parameters
    columns, rows, num_commands = list(map(int,input().split()))
    canvas = [[-1]*columns for i in range(rows)]
    commands = []
    for i in range(num_commands):
        commands.append(list(map(str,input().split())))

    for i in range(num_commands):
        if (commands[i][0] == 'C'):
            canvas = clear(commands[i],canvas)
        if (commands[i][0] == 'R'):
            canvas = rectangle(commands[i],canvas)
        if (commands[i][0] == 'S'):
            canvas = substitute(commands[i],canvas)
        if (commands[i][0] == 'P'):
            canvas = pyramid(commands[i],canvas,columns,rows)
    
    output = ''
    for row in range(rows):
        for column in range(columns):
            if canvas[row][column] == -1:
                output+='.'
            if canvas[row][column] >0:
                output+= chr(canvas[row][column])
            if column != columns-1:
                output+=' '
        if row != rows-1:
            output+='\n'
    print(output)

if __name__ == "__main__":
    main()