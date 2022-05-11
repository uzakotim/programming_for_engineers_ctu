import random
import queue

# ............................................................................
#                                 N O D E
# ............................................................................

# a node is completely identified by its number
# use abbreviation n for node


# ............................................................................
#                         B I N A R Y   T R E E
# ............................................................................

# typically root has number 0.
root = 0


def randTree(depth):
    global K, L, R, P
    n = len(K)

    # "create" a new node
    K.append(10+random.randrange(90))
    L.append(-1)
    R.append(-1)
    P.append(-1)

    if depth <= 0: return n

    # left child and whole left subtree
    if random.randrange(0, 10) < 6:
        L[n] = randTree( depth-1 )
        P[L[n]] = n
    # right child and whole right subtree
    if random.randrange(0, 10) < 6:
        R[n] = randTree( depth-1 )
        P[R[n]] = n
    return n

# ............................................................................
#               S E R V I C E   M E T H O D S    (mainly printing)
# ............................................................................

def print3(text, arr):
    print(text, end = '')
    for x in arr:
         print( ("%3d"%x), end = '')
    print()

def countNodes(n):
    if n == -1: return 0
    return 1 + countNodes( L[n]) + countNodes( R[n] )


# X is the array with coordinates, analogous to K, L, R, P

def  setXcoord( n, x_coord, X ):
    if n == -1: return x_coord
    X[n] = setXcoord( L[n], x_coord, X ) + 1
    return setXcoord( R[n],    X[n], X )

def depth( n ):
    if n == -1 : return -1;
    return 1 + max( depth(L[n]),  depth(R[n]) )

# ------------------------------------------------------------------------------------
# Display the tree using recursion to draw on canvas which is printed separately
# ------------------------------------------------------------------------------------

# X is the Inorder number of the node, the nodes are numbered
# from left to right, the number of any node W
# is bigger than the numbers of all nodes in the left subtree of W
# and it is smaller than the numbers of all nodes in the right subtree of W.

def fitNodeOnCanvas(node, depth, X, canvas, nodeWidth ):
    if node == -1 : return
    nodexpos = X[node] * nodeWidth - 1

    # print the key value on the canvas at position [depth][nodexpos]
    # to improve !! :
    canvas[depth][nodexpos] = 'X'

    # draw edges to children
    if L[node] != -1:
        for j in range( X[L[node]] * nodeWidth - 3  ,  nodexpos-2 ):
            canvas[depth][j] = '_'
    if R[node] != -1:
        for j in range(  nodexpos+1, X[R[node]] * nodeWidth   ):
            canvas[depth][j] = '_'

    fitNodeOnCanvas( L[node], depth+1, X, canvas, nodeWidth)
    fitNodeOnCanvas( R[node], depth+1, X, canvas, nodeWidth)

def display2():

    # define canvas space
    nodeWidth = 3
    Nn = countNodes(root)
    height = 1+depth(0)
    width = Nn * nodeWidth
    canvas = [['.'] * width for i in range(height)]

    # x-coord of all nodes
    X = [-1] * Nn
    setXcoord(root, 0, X)

    fitNodeOnCanvas( 0, 0, X, canvas, nodeWidth ) # start with root in depth 0

    #print(canvas)
    for row in canvas:
        for c in row:
            print(c, end = '')
        print()


# original top-down method of printing the tree,
# The tree has to be printed in a "layer by layer" fashion
# which makes code look a bit clumsy...

def display():
    Nn = countNodes(root)
    X = [-1] * Nn
    setXcoord(root, 0, X)

    qu = queue.Queue()
    prevDepth = -1
    prevEndX = -1
    # in the queue store pairs(node, its depth)
    qu.put( (root, 0) )
    while not qu.empty():
        node, nodeDepth = qu.get()

        LbranchSize = RbranchSize = 0
        if L[node] != -1:
            LbranchSize = (X[node] - X[L[node]])
            qu.put( (L[node], nodeDepth+1) )

        if R[node] != -1:
            RbranchSize = (X[R[node]] - X[node])
            qu.put( (R[node], nodeDepth+1) )

        LspacesSize = (X[node] - LbranchSize) - 1  # if first on a line
        if prevDepth == nodeDepth:                  # not first on line
            LspacesSize -= prevEndX

        # print the node, branches, leading spaces
        if prevDepth < nodeDepth and prevDepth > -1 : print() # next depth occupies new line
        nodelen = 3
        print( " "*nodelen*LspacesSize, end = '' )
        print( "_"*nodelen*LbranchSize, end = ''  )
        #print( "." + ("%2d"%node.key) + node.tag+".", end = '' )
        print( " " + ("%2d"%K[node]), end = ''  )
        print( "_"*nodelen*RbranchSize, end = ''  )

        # used in the next run of the loop:
        prevEndX = X[node] + RbranchSize
        prevDepth = nodeDepth
    # end of queue processing

    print("\n"+ '-'*Nn*nodelen) # finish the last line of the tree
    print3("X :", X)





# ............................................................................
#            T R E E   F U N C T I O N S
# ............................................................................

def minMaxVal(n):
    if n == -1: return 10**10, -1*10**10
    Lmin, Lmax = minMaxVal(L[n])
    Rmin, Rmax = minMaxVal(R[n])
    return  min(Lmin, Rmin, K[n]), max(Lmax, Rmax, K[n])

def inOrder(nodeNum):
    global K, L, R
    if nodeNum == -1: return # non-existent node
    inOrder( L[nodeNum] )
    print( K[nodeNum], end = ' ')
    inOrder( R[nodeNum] )

def preOrder(nodeNum):
    global K, L, R
    if nodeNum == -1: return # non-existent node
    print( K[nodeNum], end = ' ')
    preOrder( L[nodeNum] )
    preOrder( R[nodeNum] )



# ............................................................................
#                M A I N   P R O G R A M
# ............................................................................

random.seed( 1038 )

K, L, R, P  = [], [], [], []
randTree( 4 )
inOrder(0)
print()
preOrder(0)
print()
print(minMaxVal(0))

display()

print("---" + "---" * len(K))


nums = list(range(len(K)))
print3("    ", nums)
print("---" + "---" * len(K))
print3("K: ", K)
print3("L: ", L)
print3("R: ", R)
print3("P: ", P)

print()
print( depth(0) )

display2()

'''
Using the random seed 1038, and depth 4
the tree should be as follows:

                  _______________ 24___
      ____________ 42______          89_________
   ___ 25______      ___ 81___         ______ 32______
___ 72   ___ 15___    62    60___       40___   ___ 12___
 68       87    44             18          10    70    78
'''


