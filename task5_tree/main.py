import time
from unittest import result

class Node:
    def __init__(self,key,depth,SR,Parent):
        self.left = None
        self.right = None
        self.parent = Parent
        self.tree = None
        self.depth = depth

        self.key = key
        self.SR  = SR
        self.SK  = None
        self.CTN = 0
        self.COL = 0



class Tree:
    def __init__(self,key,depth,SR):
        self.root = Node(key,depth,SR,None)
        self.maximal = 0
        self.counter = 0
        self.counterL1 = 0
        self.counterSiblings = 0
        self.sumAllCosts = 0
    
    def rndTree(self, node, depth):
        if depth<=0: return node
        if node.SR < input_list[2] or node.depth == input_list[5]:
            node.left  = None
            node.right = None
            return node
        KeyL = (input_list[0]*(node.key+1))%input_list[6]
        KeyR = (input_list[1]*(node.key+2))%input_list[6]
        SRL  = (node.SR*input_list[0])%input_list[6]
        SRR  = (node.SR*input_list[1])%input_list[6]
        if input_list[2] <= node.SR and node.SR<input_list[3]:
            childNodeLeft   = Node (KeyL,(node.depth + 1),SRL,node)
            node.left = self.rndTree(childNodeLeft, depth-1)
            self.sumAllCosts += childNodeLeft.key*(childNodeLeft.depth+1) 
            node.right = None
            return node
        if input_list[3] <= node.SR and node.SR < input_list[4]:
            node.left = None
            childNodeRight  = Node (KeyR,(node.depth + 1),SRR,node)
            self.sumAllCosts += childNodeRight.key*(childNodeRight.depth+1) 
            node.right = self.rndTree(childNodeRight, depth-1)
            return node
        if input_list[4] <= node.SR and node.SR < input_list[6]:
            childNodeLeft   = Node (KeyL,(node.depth + 1),SRL,node)
            childNodeRight  = Node (KeyR,(node.depth + 1),SRR,node)
            self.sumAllCosts += childNodeLeft.key*(childNodeLeft.depth+1) 
            self.sumAllCosts += childNodeRight.key*(childNodeRight.depth+1) 
            node.left = self.rndTree(childNodeLeft,depth-1) 
            node.right = self.rndTree(childNodeRight,depth-1)
            return node

    # TASK 2
    def sumKeys(self,node):
        if node == None: return 0
        node.SK = node.key + self.sumKeys(node.left) + self.sumKeys(node.right)
        return node.SK

    def disbalance(self,node):  
        if node == None or (node.left == None and node.right==None): return 0
        if node.right == None: return node.left.SK  + self.disbalance(node.left) + self.disbalance(node.right) 
        if node.left  == None: return node.right.SK + self.disbalance(node.left) + self.disbalance(node.right) 

        i = (node.left.SK - node.right.SK)
        if i > 0:
            return i + self.disbalance(node.left) + self.disbalance(node.right) 
        else:
            return -i + self.disbalance(node.left) + self.disbalance(node.right) 
    
    # TASK 3
    def countTwoNodes(self,node):
        if node == None: return 0
        if (node.left != None and node.right != None):
            node.CTN += 1 + self.countTwoNodes(node.left) + self.countTwoNodes(node.right)
            return node.CTN
        else:
            node.CTN += 0 + self.countTwoNodes(node.left) + self.countTwoNodes(node.right)
            return node.CTN

    def isTwoBalanced(self,node):
        if node.left == None and node.right == None:
            return True
        if node.left != None and node.right == None:
            if node.left.CTN == 0: return True
            else: return False
        if node.left == None and node.right != None:
            if node.right.CTN == 0:return True
            else: return False

        if (node.left.CTN == node.right.CTN): return True
        else: return False

    def sumKeys2Balanced(self,node):
        if node == None: return 0
        if self.isTwoBalanced(node): 
            i = node.key
        else: 
            i = 0
        return i + self.sumKeys2Balanced(node.left) + self.sumKeys2Balanced(node.right)
   
    # Task 4   
    def countSiblings(self,node):
        if node == None: return
        if node.left != None and node.right!=None:
            if (node.left.key%2) == (node.right.key%2):
                self.counterSiblings += 1
        self.countSiblings(node.left)
        self.countSiblings(node.right)

    # TASK 5
    def isMinimal(self,node, key):
        if node == None:    return True
        if node.key >= key: return True and (self.isMinimal(node.left,key) and self.isMinimal(node.right,key))
        if node.key < key:  return False and (self.isMinimal(node.left,key) and self.isMinimal(node.right,key))

    def sumKeysMinimal(self,node):
        if node == None: return 0
        if self.isMinimal(node,node.key):       return node.key + self.sumKeysMinimal(node.left) + self.sumKeysMinimal(node.right)
        else:                                   return 0 + self.sumKeysMinimal(node.left) + self.sumKeysMinimal(node.right)
        
    # TASK 6
    def findMaxLeafKey(self,node):
        if node == None: return 0
        if (node.left==None and node.right==None):
            return node.key
        return max(self.findMaxLeafKey(node.left), self.findMaxLeafKey(node.right))
    
    def findMaximalsForAllTrees(self,node):
        if node == None or (node.left == None and node.right == None): 
            return
        if node.key>=self.findMaxLeafKey(node):   
            self.counter +=1
        self.findMaximalsForAllTrees(node.left)
        self.findMaximalsForAllTrees(node.right)
    
    # TASK 7
    def countOnlyLeft(self,node):
        if node == None: return 0
        if (node.left != None and node.right == None):
            node.COL = 1 + self.countOnlyLeft(node.left) + self.countOnlyLeft(node.right)
            return node.COL
        if (node.left == None and node.right != None):
            node.COL = -10000000000 + self.countOnlyLeft(node.left) + self.countOnlyLeft(node.right)
            return node.COL
        
        node.COL = 0 + self.countOnlyLeft(node.left) + self.countOnlyLeft(node.right)
        return node.COL 
    
    def countL1(self,node):
        if node == None: return
        if (node.COL>0):
            self.counterL1+=1
        self.countL1(node.left)
        self.countL1(node.right)
    
    # TASK 8     

    def customFindPathes(self,node,path):
        if node == None : return
        path.append(node.key)
        maximal_value = self.maximal
        current_sum = path[0]

        for i in range(len(path)-1):
            if path[i]<=path[i+1]:
                current_sum += path[i+1]
            else:
                if current_sum>=maximal_value:
                    self.maximal = current_sum
                current_sum = 0 + path[i+1]
        
        if current_sum>=maximal_value:
            self.maximal = current_sum
        
        self.customFindPathes(node.left,path)
        self.customFindPathes(node.right,path)
        path.pop()
        


if __name__ == '__main__':
   
    # input_list = [
    # 'AL',
    # 'AR',
    # 'C0',
    # 'CL',
    # 'CR',
    # 'D',
    # 'M',
    # 'RK',
    # 'RSR']
    input_list = [int(val)for val in input().split(' ')]
    start_time = time.time()
    t = Tree(input_list[7],0,input_list[8])    
    t.rndTree(t.root, input_list[5])
    
    output = ''
    t.sumAllCosts += t.root.key
    output += str(t.sumAllCosts)
    output+= '\n'
    
    t.sumKeys(t.root)
    output+= str(t.disbalance(t.root))
    output+= '\n'
    
    t.countTwoNodes(t.root)
    output+= str(t.sumKeys2Balanced(t.root))
    output+= '\n'
    
    t.countSiblings(t.root)
    output+=str(t.counterSiblings)
    output+= '\n'
 
    output += str(t.sumKeysMinimal(t.root))
    output+= '\n'

    t.findMaximalsForAllTrees(t.root)
    output+=str(t.counter)
    output+= '\n'
    
    
    t.countOnlyLeft(t.root)
    t.countL1(t.root)
    output += str(t.counterL1)
    output+= '\n'
 
    t.customFindPathes(t.root,[])
    output+=str(t.maximal)
 
    print(output) 
    
    print("--- %s seconds ---" % (time.time() - start_time))