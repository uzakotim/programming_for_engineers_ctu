<<<<<<< HEAD
#------------------------------------------------------------------------
#   Task 7 Tiles. Solved by: Timur Uzakov. 2022                         |                                            |
#------------------------------------------------------------------------
import sys
=======
import fileinput
>>>>>>> 0b2e326071490a5ea41cdb046e4c9fcd1a8bb21c

class Tile:
    def __init__(self):
        self.tileNumber  = 0
<<<<<<< HEAD
        self.widthValue  = 0
        self.heightValue = 0


def main():
    results = []
    while True:
        user_input = input()
        if user_input == '\end':
            break
        else:
            results+=user_input.split(' ')
    print(results)
=======
        self.text = []
        self.widthValue  = 0
        self.heightValue = 0
        

def readLines():
    result = []
    for line in fileinput.input():
        result+=line.rstrip().split()
    return result 

def makeTiles(input_list):
    # compare two strings i and i+1
    # if length is increasing: separate and start new tile
    # if length is = or decreasing: append to the tile 

    counter = 1
    tiles = []
    new_tile = Tile()
    new_tile.tileNumber = counter
    new_tile.text.append(input_list[0])

    for i in range(len(input_list)-1):
        if len(input_list[i+1]) <= len(input_list[i]):
            new_tile.text.append(input_list[i+1])
        else:
            tiles.append(new_tile)
            counter+=1
            new_tile = Tile()
            new_tile.tileNumber = counter
            new_tile.text.append(input_list[i+1])

    tiles.append(new_tile)
    return tiles

def calculateParameters(tiles):
    for tile in tiles:
        tile.heightValue = len(tile.text)       #calculating number of words
        tile.widthValue  = len(tile.text[0])    #calculating max width
        tile.text = tile.text[::-1]             #reversing order
    return tiles

def printTile(tile):
    output = ""
    
    maximal_space = max([len(str(tile.widthValue)),len(str(tile.heightValue)),len(str(tile.tileNumber))])
    if len(str(tile.heightValue)) >= len(str(tile.widthValue)) and len(str(tile.heightValue))!=1 :
        maximal_space -= 1

    line_height = '|'+' Height:'+maximal_space*' '+str(tile.heightValue)+' '+'|' 
    n = len(line_height)

    border  = '+'
    border += '-'*(n-2)
    border += '+'


    output+=border
    output+='\n'

    line = '|'+' Tile:'+str(tile.tileNumber)+' '+'|'
    line= '|'+' Tile:'+' '*(n-len(line)) +str(tile.tileNumber)+' '+'|'
    
    output+=line
    output+='\n'

    
    k = tile.widthValue+2

    line = '|'+' Width:'+str(tile.widthValue)+' '+'|'
    line = '|'+' Width:' + (n-len(line))*' ' +str(tile.widthValue)+' '+'|'
    output+=line
    output+='\n'

    output+=line_height
    output+='\n'
    
    
    
    border = '+'
    if k<n:
        border+='-'*tile.widthValue
        border+='+'
        border+='-'*(n-k-1)
        border+='+'
    elif n<k:
        border+='-'*(n-2)
        border+='+'
        border+='-'*(k-n-1)
        border+='+'
    else:
        border = ''
        border += '+'
        border += tile.widthValue*'-'
        border += '+'


    output+=border
    
    output+='\n'
    
    for body_line in tile.text:
        line = ''
        line +='|'
        line += (tile.widthValue-len(body_line))*' '
        line += body_line
        line +='|'
        output+=line
        output+='\n'
    
    border = ''
    border += '+'
    border += tile.widthValue*'-'
    border += '+'

    output+=border
    return output

def main():
    input_list = readLines()
    tiles = makeTiles(input_list)
    tiles = calculateParameters(tiles)
    
    output = ''
    for tile in tiles:
        output+=printTile(tile)
        output+='\n'
    
    print(output[:-1])

>>>>>>> 0b2e326071490a5ea41cdb046e4c9fcd1a8bb21c

if __name__ == '__main__':
    main()