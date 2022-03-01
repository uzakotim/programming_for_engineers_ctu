#!/usr/bin/python3
# Programming for Engineers - KYR 2021
# Graphical Editor
# CVUT
# Timur Uzakov
import numpy as np

def clear(command, canvas,columns,rows):
    if len(command)!=5:
        print("Wrongly specified clear command, should be: C x1 y1 x2 y2")
        return 
    else:
        x1 = int(command[1])
        y1 = int(command[2])
        x2 = int(command[3])
        y2 = int(command[4])
 
    if x1<0:
        x1=0
    if x2<0:
        x2=0
    if y1<0:
        y1=0
    if y2<0:
        y2=0
    if x1>=rows:
        x1=rows
    if x2>=rows:
        x2 = rows
    if y1>=columns:
        y1  = columns
    if y2>=columns:
        y2 = columns


    canvas_np = np.array(canvas)
    canvas_np[x1:x2+1,y1:y2+1] = -1
    return list(canvas_np)

def rectangle(command, canvas,columns,rows):
    if len(command)!=6:
        print("Wrongly specified clear command, should be: R x1 y1 x2 y2 char")
        return 
    else:
        x1 = int(command[1])
        y1 = int(command[2])
        x2 = int(command[3])
        y2 = int(command[4])
        character = ord(command[5])

    if x1<0:
        x1=0
    if x2<0:
        x2=0
    if y1<0:
        y1=0
    if y2<0:
        y2=0
    if x1>=rows:
        x1=rows
    if x2>=rows:
        x2 = rows
    if y1>=columns:
        y1  = columns
    if y2>=columns:
        y2 = columns

    canvas_np = np.array(canvas)
    canvas_np[x1:x2+1,y1:y2+1] = character
    return list(canvas_np)


def substitute(command, canvas,columns,rows):
    if len(command)!=7:
        print("Wrongly specified substitute command, should be: S x1 y1 x2 y2 char char")
        return 
    else:
        x1 = int(command[1])
        y1 = int(command[2])
        x2 = int(command[3])
        y2 = int(command[4])
        character_old = ord(command[5])
        character_new = ord(command[6])
    
    if x1<0:
        x1=0
    if x2<0:
        x2=0
    if y1<0:
        y1=0
    if y2<0:
        y2=0
    if x1>=rows:
        x1=rows
    if x2>=rows:
        x2 = rows
    if y1>=columns:
        y1  = columns
    if y2>=columns:
        y2 = columns

    canvas_np = np.array(canvas)
    canvas_np[x1:x2+1,y1:y2+1][canvas_np[x1:x2+1,y1:y2+1] == character_old] = character_new

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
    start= 0
    end =0
    level =0
    while (x1+i<=x2+1-i):
        start = x1+i
        end = x2-i+1
        level = y1-i
        
        if (start<0):
            start = 0
        if (end>columns):
            end = columns
        if (level<0):
            level = 0
        if (level>=rows):
            i+=1
            continue
        canvas_np[level,start:end] = character
        
        i+=1
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
            canvas = clear(commands[i],canvas,columns,rows)
        if (commands[i][0] == 'R'):
            canvas = rectangle(commands[i],canvas,columns,rows)
        if (commands[i][0] == 'S'):
            canvas = substitute(commands[i],canvas,columns,rows)
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