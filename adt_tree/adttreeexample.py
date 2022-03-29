import random
import queue

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

    # calculates x coord = node order of in Inorder traversal
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
            nodelen = 3
            print( " "*nodelen*LspacesSize, end = '' )
            print( "_"*nodelen*LbranchSize, end = ''  )
            #print( "." + ("%2d"%node.key) + node.tag+".", end = '' )
            print( node.tag + ("%2d"%node.key), end = ''  )
            print( "_"*nodelen*RbranchSize, end = ''  )

            # used in the next run of the loop:
            prevEndX = node.xcoord + RbranchSize
            prevDepth = nodeDepth
        # end of queue processing

        N = self.countNodes( self.root )
        print("\n"+ '-'*N*nodelen) # finish the last line of the tree


    # ........................................................................
    #   C U S T O M   F U N C T I O N (S),   T E S T E D  I N   M A I N (below)

    # mirror image of the original tree
    def flipTree(self, node):
        if node == None: return None
        leftTree = self.flipTree( node.left )
        rightTree = self.flipTree( node.right )
        node.left, node.right = rightTree, leftTree
        return node

# ............................................................................
#                M A I N   P R O G R A M
# ............................................................................


#initialize the random number generator
random.seed( 1038 )

# create a tree with a single node -- root.
t = BinaryTree( 0 )

# create random tree with maximum depth 4
t.rndTree( t.root, 4 )

# display the created tree
t.display()

# ------------------------------
# apply a function to the tree
t.flipTree( t.root )
# ------------------------------

# display modified tree
t.display()

# the output should be:
'''
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


