import fileinput

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

    return l_blocks


def printBlocks(l_block):
    output= ''
    
    border_prev = []
    border_prev.append(1)
    for tile in l_block[0]:
        border_prev+=[0 for _ in range(tile.widthValue)]
        border_prev+=[1]
    
    
    for block in l_block:
        height = 0

        for tile in block:
            if height<tile.heightValue:
                height = tile.heightValue  

        # Pring Border
        border = []
        border.append(1)
        for tile in block:
            border+=[0 for _ in range(tile.widthValue)]
            border+=[1]
        
        # Combining previous and current borders
        new_border = []
        for i in range(max(len(border),len(border_prev))):
                try:
                    new_border.append(border[i]+border_prev[i])
                except:
                    try:
                        new_border.append(border[i])
                    except:
                        new_border.append(border_prev[i])



        # Conversion
        for i in new_border:
            if i > 0:
                output+='+'
            else:
                output+='-'
        output+='\n'

        # Pring block information
        lines = []

        for i in reversed(range(height)): 
            line = '|'
            for tile in block:
                try:
                    l_word = len(tile.text[::-1][i])
                    if l_word < tile.widthValue:
                        line+=(tile.widthValue-l_word)*' '
                    line+= tile.text[::-1][i]
                except:
                    line += tile.widthValue*' '
                line+='|'
            lines.append(line)

        for line in lines:
            output+=line
            output+='\n'
        border_prev = border
        # ------------------------------
    # Conversion
    for i in border_prev:
        if i > 0:
            output+='+'
        else:
            output+='-'
    return output

def main():
    block_width= int(input())
    input_list = readLines()
    tiles = makeTiles(input_list)
    tiles = calculateParameters(tiles)
    l_blocks = makeBlocks(tiles,block_width)
    output = ''
    output = printBlocks(l_blocks)
    print(output)
    
if __name__ == '__main__':
        main()