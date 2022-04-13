from logging import root
import time


# input_list = [
#     'AL',
#     'AR',
#     'C0',
#     'CL',
#     'CR',
#     'D',
#     'M',
#     'RK',
#     'RSR']

input_list = [0]*9


#-----------------------------
#           NODE
#-----------------------------
class Node:
    def __init__(self,key,depth,SR,Parent):
        self.left = None
        self.right = None
        self.parent = Parent
        self.tree = None
        self.depth = depth

        self.key = key
        self.SR = SR
        self.SK = None

#-----------------------------
#         BINARY TREE
#-----------------------------
class Tree:
    def __init__(self,key,depth,SR):
        self.root = Node(key,depth,SR,None)
        self.pathes = []
        self.maximal = 0
    
    def rndTree(self, node, depth):
        if depth<=0: return node
        if node.SR < input_list[2] or node.depth == input_list[5]:
            node.left = None
            node.right = None
            return node

        if input_list[2] <= node.SR and node.SR<input_list[3]:
            childNodeLeft   = Node ((input_list[0]*(node.key+1))%input_list[6],(node.depth + 1),(node.SR*input_list[0])%input_list[6],node)
            node.left = self.rndTree(childNodeLeft, depth-1)
            node.right = None
            return node
        if input_list[3] <= node.SR and node.SR < input_list[4]:
            node.left = None
            childNodeRight  = Node ((input_list[1]*(node.key+2))%input_list[6],(node.depth + 1),(node.SR*input_list[1])%input_list[6],node)
            node.right = self.rndTree(childNodeRight, depth-1)
            return node
        if input_list[4] <= node.SR and node.SR < input_list[6]:
            childNodeLeft   = Node ((input_list[0]*(node.key+1))%input_list[6],(node.depth + 1),(node.SR*input_list[0])%input_list[6],node)
            childNodeRight  = Node ((input_list[1]*(node.key+2))%input_list[6],(node.depth + 1),(node.SR*input_list[1])%input_list[6],node)
            node.left = self.rndTree(childNodeLeft,depth-1) 
            node.right = self.rndTree(childNodeRight,depth-1)
            return node
    # TASK 1
    def sumCosts(self,node):
        if node == None: return 0
        return node.key*(node.depth+1) + self.sumCosts(node.left) + self.sumCosts(node.right)
    
   
    # TASK 2
    def sumKeys(self,node):
        if node == None: return 0
        node.SK = node.key + self.sumKeys(node.left) + self.sumKeys(node.right)
        return node.SK

    def disbalance(self,node):  
        if node == None or (node.left == None and node.right==None): return 0
        if node.left == None:
            one = 0
        else:
            one = node.left.SK
        if node.right == None:
            two = 0
        else:
            two = node.right.SK
        if one> two:
            return one - two + self.disbalance(node.left) + self.disbalance(node.right)
        else:
            return two - one + self.disbalance(node.left) + self.disbalance(node.right)
    # TASK 3
    def isTwoNode(self,node):
        if node.left != None and node.right != None:
            return True
        else: 
            return False

    def countTwoNodes(self,node):
        if node == None: return 0
        if self.isTwoNode(node):
            result = 1
        else:
            result = 0
        return result + self.countTwoNodes(node.left) + self.countTwoNodes(node.right)

    def isTwoBalanced(self,node):
        if node.left == None and node.right == None:
            return True
        if node.left != None and node.right == None:
            return False

        if node.left == None and node.right != None:
            return False

        if (self.countTwoNodes(node.left) == self.countTwoNodes(node.right)):
            return True
        else: 
            return False

    def sumKeys2Balanced(self,node):
        if node == None: return 0
        if self.isTwoBalanced(node):
            result = node.key
        else:
            result = 0
        return result + self.sumKeys2Balanced(node.left) + self.sumKeys2Balanced(node.right)
    # Task 4
    def isSibling(self,nodeOne,nodeTwo):
        #suspicious 
        if nodeOne == None or nodeTwo==None:
            return False
        #suspicious

        if nodeOne.parent == nodeTwo.parent:
            return True
        else: 
            return False         

    def isParitySibling(self,nodeOne,nodeTwo):
        if self.isSibling(nodeOne,nodeTwo):
            if (nodeOne.key%2) == (nodeTwo.key%2):
                return True
        else:
            return False
    def countSiblings(self,node):
        if node == None: return 0
        
        if self.isParitySibling(node.left,node.right):
            result = 1
        else:
            result = 0

        return result+ self.countSiblings(node.left) + self.countSiblings(node.right)
    # TASK 5
    def isMinimal(self,node, key):
        if node ==None :
            return True
        if node.key >= key:
            result = True
        if node.key < key:
            result = False
        return result and (self.isMinimal(node.left,key) and self.isMinimal(node.right,key))

    def sumKeysMinimal(self,node):
        if node == None: return 0
        if self.isMinimal(node,node.key):
            result = node.key
        else:
            result = 0
        return result + self.sumKeysMinimal(node.left) + self.sumKeysMinimal(node.right)
    # TASK 6
    def isLeaf(self,node):
        return (node.left==None and node.right==None)

    def isWeakly(self,node,key):
        result = True
        if node ==None : return True
        if node.left == None and node.right == None:
            if node.key <= key:
                result = True 
            else:
                result = False
        if node.left == None and node.right!=None:
            return result and self.isWeakly(node.right,key)
        if node.right == None and node.left!=None:
            return result and self.isWeakly(node.left,key)

        return result and (self.isWeakly(node.left,key) and self.isWeakly(node.right,key))

    def countWeakly(self,node):
        if node == None: return 0
        if self.isWeakly(node,node.key) and not self.isLeaf(node):
            result = 1
        else:
            result = 0
        return result + self.countWeakly(node.left) + self.countWeakly(node.right)

    # TASK 7

    def countOnlyLeft(self,node):
        if node == None: return 0
        if not (node.right != None and node.left == None):
            if (node.left != None and node.right == None):
                return 1 + self.countOnlyLeft(node.left) + self.countOnlyLeft(node.right)
            else:
                return 0 + self.countOnlyLeft(node.left) + self.countOnlyLeft(node.right)
        else:
            return -10000000
    
    def countL1(self,node):
        if node == None: return 0
        if (self.countOnlyLeft(node)>0):
            return 1 + self.countL1(node.left) + self.countL1(node.right)
        else:
            return 0 + self.countL1(node.left) + self.countL1(node.right)
    
    # TASK 8     

    def findPathes(self,node,path):
        if node == None: return 
        path.append(node.key)
        if len(path)>=2 and self.isSortedPath(path):
            cur_maximal = sum(path)
            if cur_maximal>=self.maximal:
                self.maximal = cur_maximal

        self.findPathes(node.left,path)
        self.findPathes(node.right,path)
        path.pop()
    
    def findAllPathes(self,node):
        if node == None: return
        path =[]
        self.findPathes(node,path)
        self.findAllPathes(node.left)
        self.findAllPathes(node.right)
    
    def isSortedPath(self,path):
        flag = True
        for i in range(len(path)-1):
            if path[i+1]>=path[i]:
                flag = True
            else:
                flag = False
                break
        return flag


if __name__ == '__main__':
   
    result = input().split(' ')
    start_time = time.time()
    for i,val in enumerate(result):
        input_list[i] = int(val)
    t = Tree(input_list[7],0,input_list[8])    
    t.rndTree(t.root, input_list[5])

    # print(t.sumCosts(t.root))
    t.sumKeys(t.root)
    print(t.disbalance(t.root))
    # print(t.sumKeys2Balanced(t.root))
    # print(t.countSiblings(t.root))
    # print(t.sumKeysMinimal(t.root))
    # print(t.countWeakly(t.root))
    # print(t.countL1(t.root))
    # t.findAllPathes(t.root)
    print("--- %s seconds ---" % (time.time() - start_time))