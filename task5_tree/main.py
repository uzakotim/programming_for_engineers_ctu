
from numpy import true_divide


input_list = [
    'AL',
    'AR',
    'C0',
    'CL',
    'CR',
    'D',
    'M',
    'RK',
    'RSR']

input_dict = {
}   

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

#-----------------------------
#         BINARY TREE
#-----------------------------
class Tree:
    def __init__(self,key,depth,SR):
        self.root = Node(key,depth,SR,None)
        self.pathes = []
        self.sums = []
    
    def rndTree(self, node, depth):
        if depth<=0: return node
        if node.SR < input_dict['C0'] or node.depth == input_dict['D']:
            node.left = None
            node.right = None
            return node

        if input_dict['C0'] <= node.SR and node.SR<input_dict['CL']:
            childNodeLeft   = Node ((input_dict['AL']*(node.key+1))%input_dict['M'],(node.depth + 1),(node.SR*input_dict['AL'])%input_dict['M'],node)
            node.left = self.rndTree(childNodeLeft, depth-1)
            node.right = None
            return node
        if input_dict['CL'] <= node.SR and node.SR < input_dict['CR']:
            node.left = None
            childNodeRight  = Node ((input_dict['AR']*(node.key+2))%input_dict['M'],(node.depth + 1),(node.SR*input_dict['AR'])%input_dict['M'],node)
            node.right = self.rndTree(childNodeRight, depth-1)
            return node
        if input_dict['CR'] <= node.SR and node.SR < input_dict['M']:
            childNodeLeft   = Node ((input_dict['AL']*(node.key+1))%input_dict['M'],(node.depth + 1),(node.SR*input_dict['AL'])%input_dict['M'],node)
            childNodeRight  = Node ((input_dict['AR']*(node.key+2))%input_dict['M'],(node.depth + 1),(node.SR*input_dict['AR'])%input_dict['M'],node)
            node.left = self.rndTree(childNodeLeft,depth-1) 
            node.right = self.rndTree(childNodeRight,depth-1)
            return node
    # TASK 1
    def sumCosts(self,node):
        if node == None: return 0
        return node.key*(node.depth+1) + self.sumCosts(node.left) + self.sumCosts(node.right)
    
    def sumKeys(self,node):
        if node == None: return 0
        return node.key + self.sumKeys(node.left) + self.sumKeys(node.right)

    # TASK 2
    def disbalance(self,node):  
        # if empty
        if node == None or (node.left == None and node.right==None): return 0
        # if not empty and there are children
        one = self.sumKeys(node.left)
        two = self.sumKeys(node.right)
        if one> two:
            return one - two
        else:
            return two - one

    def sumDisbalance(self,node):
        if node == None:
            return 0
        return self.disbalance(node) + self.sumDisbalance(node.left) + self.sumDisbalance(node.right)
        


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
    def hasOnlyLeft(self,node):
        if node.left != None and node.right == None:
            return True
        else:
            return False
    def hasOnlyRight(self,node):
        if node.right != None and node.left == None:
            return True
        else:
            return False

    def countOnlyLeft(self,node):
        if node == None: return 0
        if not self.hasOnlyRight(node):
            if self.hasOnlyLeft(node):
                return 1 + self.countOnlyLeft(node.left) + self.countOnlyLeft(node.right)
            else:
                return 0 + self.countOnlyLeft(node.left) + self.countOnlyLeft(node.right)
        elif self.hasOnlyRight(node):
            return -10000000
    
    def isL1(self,node):
        if (self.countOnlyLeft(node)>0):
            return True
        else:
            return False

    def countL1(self,node):
        if node == None: return 0
        if self.isL1(node):
            return 1 + self.countL1(node.left) + self.countL1(node.right)
        else:
            return 0 + self.countL1(node.left) + self.countL1(node.right)
    
    # TASK 8    
    def findPathes(self,node,path):
        if node == None:
            return 
        path.append(node.key)
        if len(path)>=2 and self.isSortedPath(path):
            self.sums.append(sum(path))

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
    for i,val in enumerate(result):
        input_dict[input_list[i]] = int(val)

    t = Tree(input_dict['RK'],0,input_dict['RSR'])
    
    t.rndTree(t.root, input_dict['D'])
    # t.findAllPathes(t.root)
    print(t.sumCosts(t.root))
    print(t.sumDisbalance(t.root))
    print(t.sumKeys2Balanced(t.root))
    print(t.countSiblings(t.root))
    print(t.sumKeysMinimal(t.root))
    print(t.countWeakly(t.root))
    print(t.countL1(t.root))
    t.findAllPathes(t.root)
    print(max(t.sums))