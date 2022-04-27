#------------------------------------------------------------------------
#   Binary Adjacency List. Solved by: Timur Uzakov. 2022                |
#------------------------------------------------------------------------

from platform import node
import re
import time
debug = False # set to True, in case you need to track execution time

class Graph:
    def __init__(self, n,colors):
        self.adjacency_black = colors
        self.adjacency_white = [1 - x for x in colors]
        self.left  = n*[None]
        self.right = n*[None]
        self.number_of_node_in_tree = 0
        self.L = 0
        self.E = 0
        self.R = 0
        self.b = n*[None]
        self.w = n*[None]
        self.nodes = n*[None]
        self.counter = 0

    def countBlack(self,head):
        self.counter += 1
        if head == None: return 0
        self.b[head] = self.adjacency_black[head] + self.countBlack(self.left[head]) + self.countBlack(self.right[head]) 
        return self.b[head]

    def countWhite(self,head):
        self.counter += 1
        if head == None: return 0
        self.w[head] = self.adjacency_white[head] + self.countWhite(self.left[head]) + self.countWhite(self.right[head]) 
        return self.w[head]

if __name__ == '__main__':
    if debug: start_time = time.time()
#------------------------------------------------------------------------
#   Input and graph building                                            |
#------------------------------------------------------------------------
    n = int(input())
    
    list_of_colors = [int(color) for color in input().split(' ')]
    graph = Graph(n,list_of_colors) 

    for i in range(n-1):
        edge = [int(x) for x in input().split(' ')]
        if edge[2] == 0:
            graph.left[edge[0]] = edge[1]
        else:
            graph.right[edge[0]] = edge[1]

#------------------------------------------------------------------------
#   If statements that compare the white,black,wwhite and bblack values |
#------------------------------------------------------------------------   
    graph.countWhite(0)
    graph.countBlack(0)

    for i in range(n):
        var_left  = None
        var_right = None

        if graph.left[i]:
            b = graph.b[graph.left[i]]
            w = graph.w[graph.left[i]]
            if b != 0:
                var_left = w/b
            else:
                var_left = None
        else:
            b = 0
            w = 0
            var_left = None

        if graph.right[i]:
            bb = graph.b[graph.right[i]]
            ww = graph.w[graph.right[i]]
            if bb != 0:
                var_right = ww/bb
            else:
                var_right = None
        else:
            bb = 0 
            ww = 0
            var_right = None

        if var_left and var_right:
            if   var_left > var_right:  graph.L+=1
            elif var_left == var_right: graph.E+=1
            elif var_left < var_right:  graph.R+=1 

#------------------------------------------------------------------------
#   Printing                                                            |
#------------------------------------------------------------------------
    output = ''
    output+= str(graph.L)
    output+= ' '
    output+= str(graph.E)
    output+= ' '
    output+= str(graph.R)
    if debug: print(50*'*')
    print(output) 
    if debug: print("--- %s seconds ---" % ((time.time() - start_time)))
    # print(graph.counter)
    # print(graph.b)
    # print(graph.w)