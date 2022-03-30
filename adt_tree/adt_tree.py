import random
import queue


# ............................................................................
#                                 N O D E
# ............................................................................

class Node:
    def __init__(self, key):
        # mandatory
        self.left = None
        self.right = None
        self.key = key
        # extra
        self.xcoord = -1
        self.tag = ' ' # one character

    def print(self):
        print( "[" + str(self.key) + "]", end = "" )
        print( str(self.xcoord)+", ", end = "")


# ............................................................................
#                         B I N A R Y   T R E E
# ............................................................................

# Tree manipulation not implemented directrly in Python
# Neither in C,C++,C#,PHP,Java
# Reason: many different types of trees 


class BinaryTree:
    def __init__(self, key ):
        self.root = Node( key )

    def rndTree(self, node, depth):
        # RANDOM TREE GENERATION
        # Recursive scheme
        # 1) Create root
        # 2) Create smaller random tree and 
        # set its root to be the left child of the of 
        # the children root
        # 3) Repeat at right 
        # 4) Stop recursion


        node.key = 10 +random.randrange(90)
        if depth <= 0:  return node

        if random.randrange(0, 10) < 6: #regulation of tree creation
            # new constructor - new node
            childNode = Node ( 0 )  # any key will do
            node.left = self.rndTree( childNode, depth-1 )

        if random.randrange(0, 10) < 6:
            childNode = Node ( 0 )  # any key will do
            node.right = self.rndTree( childNode, depth-1 )
        return node

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
            nodelen = 2
            print( " "*nodelen*LspacesSize, end = '' )
            print( "_"*nodelen*LbranchSize, end = ''  )
            #print( "." + ("%2d"%node.key) + node.tag+".", end = '' )
            #print( node.tag + ("%2d"%node.key), end = ''  )
            print( "" + ("%2d"%node.key), end = ''  )
            print( "_"*nodelen*RbranchSize, end = ''  )

            # used in the next run of the loop:
            prevEndX = node.xcoord + RbranchSize
            prevDepth = nodeDepth
        # end of queue processing

        N = self.countNodes( self.root )
        print("\n"+ '-'*N*nodelen) # finish the last line of the tree

    def countAllNodes(self, node):
        if node == None: return 0
        return     self.countAllNodes(node.left) + \
               1 + self.countAllNodes(node.right)

    def countInternalNodes(self, node):
        if node == None: return 0
        if node.left == None and node.right == None: return 0
        return       self.countInternalNodes(node.left)\
               + 1 + self.countInternalNodes(node.right)

    def countLeaves(self, node):
        if node == None: return 0
        if node.left == None and node.right == None: return 1
        return self.countLeaves(node.left) + self.countLeaves(node.right)

    def countNodesWith1child(self, node):
        if node == None: return 0
        if node.left == None and node.right != None:
            return 1 + self.countNodesWith1child( node.right )
        if node.right == None and node.left != None:
            return 1 + self.countNodesWith1child( node.left )
        return   self.countNodesWith1child(node.left) \
               + self.countNodesWith1child(node.right)

    def countNodesWith2children(self, node):
        if node == None: return 0
        if node.left != None and node.right != None:
            # print( " node with 2 children, key:", node.key)
            return 1 + self.countNodesWith2children(node.left) \
                     + self.countNodesWith2children(node.right)
        return     self.countNodesWith2children(node.left) \
                 + self.countNodesWith2children(node.right)

    def keysToDepths(self, node, depth):
        if node == None: return
        node.key = depth
        self.keysToDepths( node.left, depth + 1 )
        self.keysToDepths( node.right, depth + 1 )

    # node height == distance form node to its deepest descendant
    # leaf height = 0
    def keysToHeights(self, node ):
        if node == None: return -1
        height = 1 + max( self.keysToHeights(node.left), \
                          self.keysToHeights(node.right) )
        node.key = height
        return height

    def insertLeftmost(self, node, key):
        if node.left == None:
            node.left = Node(key)
            return
        self.insertLeftmost( node.left, key )

    def deleteAllLeaves(self, node):
        childL = node.left
        childR = node.right

        if childL != None:
            if childL.left == childL.right == None:
                node.left = None
            else:
                self.deleteAllLeaves( childL )

        if childR != None:
            if childR.left == childR.right == None:
                node.right = None
            else:
                self.deleteAllLeaves( childR )

    # this variant returns true from a leaf and false form a non-leaf
    # it simplifies checking of the left and the right child
    def deleteAllLeaves2(self, node):
        childL = node.left
        childR = node.right

        if childL.left == childL.right == None:
            return True # node is a leaf

        if self.deleteAllLeaves( childL ) == True:
            node.left = None

        if self.deleteAllLeaves( childR ) == True:
            node.right = None

        return False # this (was) not a leaf

    # this method supposes that the tree root has two children
    # add another method which will also correctly manipulate
    # a tree which rot has just one child
    # ---------------
    # PostOrder scheme:
    # When a node has 1 child X the function returns the reference to to X
    # and the parent automatically deletes the node by connecting to  X directly
    # when the recursion returns to the parent.
    # When a node has 0 or 2 children the reference to node itself is returned -- parent has nothing to do.
    def removeNodesWith1Child(self, node):
        if node == None: return None

        node.left = self.removeNodesWith1Child( node.left)
        node.right = self.removeNodesWith1Child( node.right)

        if node.left != None and node.right == None:
            return node.left
        if node.right != None and node.left == None:
            return node.right

        return node  # otherwise

    # mirror image of the original tree
    def flipTree(self, node):
        if node == None: return None
        LsubTree = self.flipTree( node.left )
        RsubTree = self.flipTree( node.right )
        node.left, node.right = RsubTree, LsubTree
        return node

    # when a node is a leaf with key K the function creates its two new children
    # the key of the left child is K-1 and the key of the right child is K+1
    def splitLeaves(self, node):
        if node == None: return
        if node.left == None and node.right == None:
            node.left = Node( node.key-1 )
            node.right = Node( node.key+1 )
            return
        self.splitLeaves( node.left )
        self.splitLeaves( node.right )

    # builds a complete balanced tree with the given depth
    # (the total number of nodes in this tree is 2^(depth+1) - 1
    def buildComplete(self, depth ):
        if depth < 0: return None
        node = Node( random.randrange(10,99) ) # some random key
        node.left = self.buildComplete( depth-1 )
        node.right = self.buildComplete( depth-1 )
        return node


    # removes from the tree the whole whole right subtree
    # of each node in the given depth
    def cutOffRbranch(self, node, depth ):
        if node == None: return

        if depth == 0:
            node.right = None
            return

        self.cutOffRbranch( node.left, depth-1 )
        self.cutOffRbranch( node.right, depth -1 )


# ............................................................................
#                M A I N   P R O G R A M
# ............................................................................

random.seed( 1038 )
t = BinaryTree( 0 )

print( "Random tree" )
t.rndTree( t.root, 3 )

print( "Display ")
t.display()

# example function calls

print( "The number of all nodes is", t.countAllNodes(t.root) )

print( "The number of leaves is", t.countLeaves(t.root) )

print( "The number of internal nodes is", t.countInternalNodes(t.root) )

print( "The number of nodes with 1 child is", t.countNodesWith1child(t.root) )

print( "The number of nodes with 2 children is", t.countNodesWith2children(t.root) )

print( "Set node keys to be depths")
t.keysToDepths(t.root, 0)
t.display()

print( "Set node keys to be heights")
t.keysToHeights(t.root)
t.display()

print( "Insert one leftmost node 11")
t.insertLeftmost(t.root, 11)
t.display()

print( "Delete all leaves ")
t.deleteAllLeaves(t.root)
t.display()

print( "Remove all nodes with 1 child  ")
t.removeNodesWith1Child(t.root)
t.display()

print( "Mirror the tree")
t.flipTree(t.root)
t.display()

print( "Create a regular perfectly balanced tree of given depth")
t.root = t.buildComplete(4)
t.display()

print( "Cut off each R branch in a given depth")
t.cutOffRbranch(t.root, 2)
t.display()


