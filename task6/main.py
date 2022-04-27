#------------------------------------------------------------------------
#   Binary Adjacency List. Solved by: Timur Uzakov. 2022                |                                            |
#------------------------------------------------------------------------
import time
debug = False # set to True, in case you need to track execution time

class Graph:
    def __init__(self, n,colors):
        
        self.adjacency_black = colors
        self.left  = n*[None]
        self.right = n*[None]
        self.number_of_node_in_tree = 0
        self.L = 0
        self.E = 0
        self.R = 0
  
    def count(self,head):
        if head == None: return 0  
        self.number_of_node_in_tree += 1
        return self.adjacency_black[head]   \
             + self.count(self.left[head])  \
             + self.count(self.right[head]) 

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
    for i in range(n):
        var_left  = None
        var_right = None

        if graph.left[i]:
            graph.number_of_node_in_tree = 0
            b = graph.count(graph.left[i])
            k = graph.number_of_node_in_tree
            w = k - b
            if b != 0:
                var_left = w/b
            else:
                var_left = None
        else:
            b = 0
            w = 0
            var_left = None

        if graph.right[i]:
            graph.number_of_node_in_tree = 0
            bb = graph.count(graph.right[i])
            kk = graph.number_of_node_in_tree
            ww = kk - bb
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
    if debug: print("--- %s micro seconds ---" % ((time.time() - start_time)*1000000.0))

    