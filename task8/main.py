
import fileinput

from numpy import block, tile
from yaml import BlockSequenceStartToken

class Tile:
    def __init__(self):
        self.tileNumber  = 0
        self.text = []
        self.widthValue  = 0
        self.heightValue = 0
        

def readLines():
    result = []
    for line in fileinput.input():
        result+=line.rstrip().split()
    return result 

def calculateParameters(tiles):
    for tile in tiles:
        tile.heightValue = len(tile.text)       #calculating number of words
        tile.widthValue  = len(tile.text[0])    #calculating max width
        tile.text = tile.text[::-1]             #reversing order
    return tiles

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
def makeBlocks(tiles,block_width):
    counter = 1
    l_blocks = []
    block = []

    i =0 
    while (i < len(tiles)):
        counter += tiles[i].widthValue + 1
        if counter <= block_width:
            block.append(tiles[i])
        else:
            l_blocks.append(block)
            block = []
            counter = 1
            i-=1
        i+=1
    l_blocks.append(block)



    # for tile in tiles:
    #     counter += tile.widthValue + 1
    #     if counter<=block_width:
    #         block.append(tile)
    #         print(tile.text)
    #     else:
    #         print("Block!")
    #         l_blocks.append(block)
    #         block = []
    #         counter = 1
    return l_blocks

def main():
    block_width= int(input())
    input_list = readLines()
    tiles = makeTiles(input_list)
    tiles = calculateParameters(tiles)
    l_blocks = makeBlocks(tiles,block_width)

    # check if consistent
    for block in l_blocks:
        print("Block")
        for tile in block:
            print(tile.text)



    

    
if __name__ == '__main__':
        main()