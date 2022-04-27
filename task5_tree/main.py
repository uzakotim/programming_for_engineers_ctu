import time
<<<<<<< HEAD
=======

>>>>>>> 05f5386bb7d4af339cbed9d4e91db077d18f0bb4

class Node:
    def __init__(self,key,depth,SR):
        self.left = None
        self.right = None   
        self.depth = depth

        self.key = key
        self.SR  = SR
        self.SK  = None
        self.CTN = 0
        self.COL = 0


class Tree:
    def __init__(self,key,depth,SR):
        self.root = Node(key,depth,SR)
        self.maximal = 0
        self.count   = 0
        self.counter = 0
        self.counterL1 = 0
        self.counterSiblings = 0
        self.sumAllCosts = 0
        self.sumTwoBalanced = 0
        self.sumMinimal = 0
    
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
            childNodeLeft   = Node (KeyL,(node.depth + 1),SRL)
            node.left = self.rndTree(childNodeLeft, depth-1)
            self.sumAllCosts += childNodeLeft.key*(childNodeLeft.depth+1) 
            node.right = None
            return node
        if input_list[3] <= node.SR and node.SR < input_list[4]:
            node.left = None
            childNodeRight  = Node (KeyR,(node.depth + 1),SRR)
            self.sumAllCosts += childNodeRight.key*(childNodeRight.depth+1) 
            node.right = self.rndTree(childNodeRight, depth-1)
            return node
        if input_list[4] <= node.SR and node.SR < input_list[6]:
            childNodeLeft   = Node (KeyL,(node.depth + 1),SRL)
            childNodeRight  = Node (KeyR,(node.depth + 1),SRR)
            self.sumAllCosts += childNodeLeft.key*(childNodeLeft.depth+1) 
            self.sumAllCosts += childNodeRight.key*(childNodeRight.depth+1)
            if (childNodeLeft.key%2) == (childNodeRight.key%2):
                self.counterSiblings += 1 
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

    def sumKeys2Balanced(self,node):
        if node == None: return
        if node.left == None and node.right == None:
            self.sumTwoBalanced+=node.key
            return
        elif node.left != None and node.right == None:
            if node.left.CTN == 0: 
                self.sumTwoBalanced+=node.key
        elif (node.left == None and node.right != None):
            if node.right.CTN == 0:
                self.sumTwoBalanced+=node.key
        elif (node.left.CTN == node.right.CTN): 
            self.sumTwoBalanced+=node.key

        self.sumKeys2Balanced(node.left)
        self.sumKeys2Balanced(node.right)

    # TASK 5
    def isMinimal(self,node, key):
<<<<<<< HEAD
        if node == None: return True
        if node.key >= key: 
            return True and (self.isMinimal(node.left,key) and self.isMinimal(node.right,key))
        if node.key < key:  
            return False and (self.isMinimal(node.left,key) and self.isMinimal(node.right,key))
=======
        if node == None:    return True
        if node.key >= key: return True  and (self.isMinimal(node.left,key) and self.isMinimal(node.right,key))
        if node.key < key:  return False and (self.isMinimal(node.left,key) and self.isMinimal(node.right,key))
>>>>>>> 05f5386bb7d4af339cbed9d4e91db077d18f0bb4

    def sumKeysMinimal(self,node):
        if node == None: return
        if self.isMinimal(node,node.key): self.sumMinimal += node.key
        self.sumKeysMinimal(node.left)
        self.sumKeysMinimal(node.right)

        
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
   
    start_time = time.time()
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
    
    key_list = []
    sr_list  = []
    depth_list=[]
    left_child_list =  [] # list of indexes of all left children
    right_child_list = [] # list of indexes of all right children


    # Root node    
    key_list.append(input_list[7])
    sr_list.append(input_list[8])
    depth_list.append(0)

    left_child_list.append(None)
    right_child_list.append(None)

    current = 0 # current goes through every node
    child_counter = 0

    while depth_list[current]<input_list[5]:
        if sr_list[current]< input_list[2] or depth_list[current] == input_list[5]:
            left_child_list[current]  = None
            right_child_list[current] = None

        KeyL = (input_list[0]*(key_list[current]+1))%input_list[6]
        KeyR = (input_list[1]*(key_list[current]+2))%input_list[6]
        SRL  = (sr_list[current]*input_list[0])%input_list[6]
        SRR  = (sr_list[current]*input_list[1])%input_list[6] 
        
        if input_list[2]<= sr_list[current] and sr_list[current]<input_list[3]:
            child_counter+=1
            key_list.append(KeyL)
            depth_list.append(depth_list[current]+1)
            sr_list.append(SRL)

            left_child_list[current]  = child_counter
            right_child_list[current] = None
            
            left_child_list.append(None)
            right_child_list.append(None)
            
            current+=1
            continue

        if input_list[3]<= sr_list[current] and sr_list[current]<input_list[4]:
            child_counter+=1
            key_list.append(KeyR)
            depth_list.append(depth_list[current]+1)
            sr_list.append(SRR)

            right_child_list[current] = child_counter
            left_child_list[current]  = None

            left_child_list.append(None)
            right_child_list.append(None)

            current+=1
            continue

        if input_list[4] <= sr_list[current] and sr_list[current]<input_list[6]:
            child_counter+=1
            key_list.append(KeyL)
            depth_list.append(depth_list[current]+1)
            sr_list.append(SRL)
            
            left_child_list[current]  = child_counter

            left_child_list.append(None)
            right_child_list.append(None)

            child_counter+=1
            key_list.append(KeyR)
            depth_list.append(depth_list[current]+1)
            sr_list.append(SRR)

            right_child_list[current] = child_counter

            left_child_list.append(None)
            right_child_list.append(None)
        current+=1

    output = ''
<<<<<<< HEAD


    sumCosts = 0
    for i,key in enumerate(key_list):
        sumCosts+= key*(depth_list[i]+1)
    
    output += str(sumCosts)
    output+= '\n'
=======
    # t.sumAllCosts += t.root.key
    # output += str(t.sumAllCosts)
    # output+= '\n'
    
    # t.sumKeys(t.root)
    # output+= str(t.disbalance(t.root))
    # output+= '\n'
    
    # t.countTwoNodes(t.root)
    # output+= str(t.sumKeys2Balanced(t.root))
    # output+= '\n'
    
    # t.countSiblings(t.root)
    # output+=str(t.counterSiblings)
    # output+= '\n'
 
    # output += str(t.sumKeysMinimal(t.root))
    # output+= '\n'
>>>>>>> 05f5386bb7d4af339cbed9d4e91db077d18f0bb4

    # t.sumKeys(t.root)
    # output+= str(t.disbalance(t.root))
    # output+= '\n'
    
    # t.countTwoNodes(t.root)
    # t.sumKeys2Balanced(t.root)
    # output += str(t.sumTwoBalanced)
    # output+= '\n'
    
<<<<<<< HEAD
    # output+=str(t.counterSiblings)
    # output+= '\n'
 
    # t.sumKeysMinimal(t.root)
    # output += str(t.sumMinimal)
    # output += '\n'

    # t.findMaximalsForAllTrees(t.root)
    # output+=str(t.counter)
    # output+= '\n'
    
    
    # t.countOnlyLeft(t.root)
    # t.countL1(t.root)
    # output += str(t.counterL1)
    # output+= '\n'
 
=======
    # t.countOnlyLeft(t.root)
    # t.countL1(t.root)
    # output += str(t.counterL1)
    # output+= '\n'
 
>>>>>>> 05f5386bb7d4af339cbed9d4e91db077d18f0bb4
    # t.customFindPathes(t.root,[])
    # output+=str(t.maximal)
 
    print(output) 
    
    print("--- %s seconds ---" % (time.time() - start_time))