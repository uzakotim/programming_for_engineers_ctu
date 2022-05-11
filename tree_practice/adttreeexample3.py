import random
import queue

# The program shows how a tree can be represented only by arrays of values.
# each node is assigned a unique number (label) and by that number it is
# recognized. The information related to a node, its key, the labels of
# the children and parent etc, are stored in separate arrays.
# The number (label) of the node serves as index to those arrays.
# It is therefore unnecessary to store the number(label) of the node
# anywhere in the memory.
# Below, arrays K, L, R, P store Keys, Left child number, Right child
# number, parent number, respectively, for all nodes in the tree.


# ............................................................................
#                                 N O D E
# ............................................................................

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.xcoord = -1
        self.tag = ' ' # one character
        self.num = 0

    def print(self):
        print( "[" + str(self.key) + "]", end = "" )
        print( str(self.xcoord)+", ", end = "")


# ............................................................................
#                         B I N A R Y   T R E E
# ............................................................................

class BinaryTree:

    # ........................................................................
    #   C O N S T R U C T O R
    def __init__(self, key ):
        self.root = Node( key )

    def rndTree(self, node, depth):
        node.key = 10+random.randrange(90)
        if depth <= 0:  return node

        if random.randrange(0, 10) < 6:
            childNode = Node ( 0 )  # any key will do
            node.left = self.rndTree( childNode, depth-1 )

        if random.randrange(0, 10) < 6:
            childNode = Node ( 0 )  # any key will do
            node.right = self.rndTree( childNode, depth-1 )
        return node

    # ........................................................................
    #   S E R V I C E   M E T H O D S    (mainly printing)
    def countNodes(self, node):
        if node == None: return 0
        return 1 + self.countNodes( node.left ) + self.countNodes( node.right )

    # calculates x coord = node order of  InOrder traversal
    def setXcoord(self, node, x_coord):
        if node == None: return x_coord
        node.xcoord = self.setXcoord(node.left, x_coord) + 1
        #print(node.key, node.setXcoord)
        return self.setXcoord(node.right, node.xcoord)

    def display(self):
        self.setXcoord(self.root, 0)
        qu = queue.Queue()
        prevDepth = -1
        prevEndX = -1
        # in the queue store pairs(node, its depth)
        qu.put( (self. root, 0) )
        while not qu.empty():
            node, nodeDepth = qu.get()

            LbranchSize = RbranchSize = 0
            if node.left != None:
                LbranchSize = (node.xcoord - node.left.xcoord)
                qu.put( (node.left, nodeDepth+1) )
            if node.right != None:
                RbranchSize = (node.right.xcoord - node.xcoord)
                qu.put( (node.right, nodeDepth+1) )

            LspacesSize = (node.xcoord - LbranchSize) - 1  # if first on a line
            if prevDepth == nodeDepth:                  # not first on line
                LspacesSize -= prevEndX

            # print the node, branches, leading spaces
            if prevDepth < nodeDepth and prevDepth > -1 : print() # next depth occupies new line
            nodelen = 5
            print( " "*nodelen*LspacesSize, end = '' )
            print( "_"*nodelen*LbranchSize, end = ''  )
            #print( "." + ("%2d"%node.key) + node.tag+".", end = '' )
            print( ("%2d"%node.num) +"_" + ("%2d"%node.key), end = ''  )
            print( "_"*nodelen*RbranchSize, end = ''  )

            # used in the next run of the loop:
            prevEndX = node.xcoord + RbranchSize
            prevDepth = nodeDepth
        # end of queue processing

        N = self.countNodes( self.root )
        print("\n"+ '-'*N*nodelen) # finish the last line of the tree


    # ........................................................................
    #   C U S T O M   F U N C T I O N (S)


    # ..............................................
    # returns the number of the rightmost (last one) node
    # in the subtree rooted in "node"
    def NumberPreOrder_rec(self, node, currNum):

        if node == None:
            return currNum   # no change

        # assign the number to the node
        currNum += 1
        node.num = currNum

        # go left from this node
        # and update currrent number (currMun)
        currNum = self.NumberPreOrder_rec(node.left, currNum)

        # go right from this node and update currNum again
        currNum = self.NumberPreOrder_rec(node.right, currNum)

        return currNum


    def numberPreOrder(self):
        self.NumberPreOrder_rec(self.root, -1 )

    # Setting the numbers of nodes in InOrder sequence, is a little bit more
    # tricky. In fact, it is used in the display method.
    # To assign to a node X a number which corresponds to the InOrder
    # position of the node, we must know how many nodes are there in total
    # to the left of X in the whole tree. The function setXcoord does it.

    # .....................................................................

    def intoArrays_rec(self, node, currNum, K, L, R, P):
        if node == None:
            return currNum   # no change

        # assign the number to the node
        currNum += 1
        node.num = currNum

        #initialize node in arrays
        K[node.num] = node.key
        L[node.num] = -1
        R[node.num] = -1
        P[node.num] = -1

        # go left from this node
        if node.left != None:
            currNum = self.intoArrays_rec(node.left, currNum, K, L, R, P)
            # register the link between node and its left child
            L[node.num] = node.left.num
            P[node.left.num] = node.num

        # go right from this node
        if node.right != None:
            currNum = self.intoArrays_rec(node.right, currNum, K, L, R, P)
            # register the link between node and its right child
            R[node.num] = node.right.num
            P[node.right.num] = node.num

        return currNum

    def intoArrays(self):
        countAll = self.countNodes(self.root)
        K = [-1] * countAll
        L = [-1] * countAll
        R = [-1] * countAll
        P = [-1] * countAll
        self.intoArrays_rec( self.root, -1, K, L, R, P)
        return K, L, R, P

def print3(text, arr):
    print(text, end = '')
    for x in arr:
         print( ("%3d"%x), end = '')
    print()


def inOrder(nodeNum):
    if nodeNum == -1: return # non-existent node
    inOrder( L[nodeNum] )
    print( K[nodeNum], end = ' ')
    inOrder( R[nodeNum] )



# ............................................................................
#                M A I N   P R O G R A M
# ............................................................................


# initialize the random number generator
random.seed( 1038 )

# create a tree with a single node -- root.
t = BinaryTree( 0 )

# create random tree with maximum depth 4
t.rndTree( t.root, 4 )

t.numberPreOrder()

# display the created tree
t.display()

K, L, R, P = t.intoArrays()

nums = list(range(len(K)))
print3("   ", nums)
print("---" + "---" * len(K))
print3("K: ", K)
print3("L: ", L)
print3("R: ", R)
print3("P: ", P)

print()
inOrder(0)
# ------------------------------


'''
Calling flipTree and using the random seed 1038,
the output should be as follows:
You may try other seed values as well.

                  _______________ 24___
      ____________ 42______          89_________
   ___ 25______      ___ 81___         ______ 32______
___ 72   ___ 15___    62    60___       40___   ___ 12___
 68       87    44             18          10    70    78
---------------------------------------------------------
                  ___ 24_______________
         _________ 89         ______ 42____________
   ______ 32______         ___ 81___      ______ 25___
___ 12___   ___ 40      ___ 60    62   ___ 15___    72___
 78    70    10          18             44    87       68
---------------------------------------------------------
'''


