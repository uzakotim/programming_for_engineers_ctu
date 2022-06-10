#------------------------------------------------------------------------
#   Task 7 Tiles. Solved by: Timur Uzakov. 2022                         |                                            |
#------------------------------------------------------------------------
import sys

class Tile:
    def __init__(self):
        self.tileNumber  = 0
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

if __name__ == '__main__':
    main()