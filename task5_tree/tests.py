import unittest

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
    
    def rndTree(self, node, depth):
        if depth<=0: return node
        if node.SR < input_dict['C0'] or node.depth == input_dict['D']:
            node.left = None
            node.right = None
            return node

        childNodeLeft   = Node ((input_dict['AL']*(node.key+1))%input_dict['M'],(node.depth + 1),(node.SR*input_dict['AL'])%input_dict['M'],node)
        childNodeRight  = Node ((input_dict['AR']*(node.key+2))%input_dict['M'],(node.depth + 1),(node.SR*input_dict['AR'])%input_dict['M'],node)

        if input_dict['C0'] <= node.SR and node.SR<input_dict['CL']:
            node.left = self.rndTree(childNodeLeft, depth-1)
            node.right = None
            return node
        if input_dict['CL'] <= node.SR and node.SR < input_dict['CR']:
            node.left = None
            node.right = self.rndTree(childNodeRight, depth-1)
            return node
        if input_dict['CR'] <= node.SR and node.SR < input_dict['M']:
            node.left = self.rndTree(childNodeLeft,depth-1) 
            node.right = self.rndTree(childNodeRight,depth-1)
            return node
    # TASK 1
    def sumCosts(self,node):
        if node == None: return 0
        result = node.key*(node.depth+1) + self.sumCosts(node.left) + self.sumCosts(node.right)
        return result
    
    def sumKeys(self,node):
        if node == None: return 0
        result = node.key + self.sumKeys(node.left) + self.sumKeys(node.right)
        return result

    # TASK 2
    def disbalance(self,node):  
        # if empty
        if node == None: return 0
        # if no children
        if node.left == None and node.right == None:
            return 0
        # if not empty and there are children
        total = abs(self.sumKeys(node.left) - self.sumKeys(node.right))
        return total

    def sumDisbalance(self,node):
        if node == None:
            return 0
        result = self.disbalance(node) + self.sumDisbalance(node.left) + self.sumDisbalance(node.right)
        return result


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

        

class TestStringMethods(unittest.TestCase):

    # def test_root(self):
        # self.assertEqual(t.root.key,0)
    def test_depth(self):
        self.assertEqual(t.root.depth,0)
    def test_SR(self):
        self.assertEqual(t.root.SR, input_dict['RSR'])
    def test_RK(self):
        self.assertEqual(t.root.key, input_dict['RK'])
    def test_root(self):
        self.assertEqual(t.root.key, 9)
    def test_node_left(self):
        self.assertEqual(t.root.left.key,0)
    def test_node_right(self):
        self.assertEqual(t.root.right.key,3)
    def test_node_left_SR(self):
        self.assertEqual(t.root.left.SR,4)
    def test_node_right_SR(self):
        self.assertEqual(t.root.right.SR,16)
    def test_grand_children_key(self):
        self.assertEqual(t.root.left.left.key, 12)
    def test_grand_children_SR(self):
        self.assertEqual(t.root.right.right.right.SR,4)
    def test_overall_cost(self):
        self.assertEqual(t.sumCosts(t.root), 494)
    def test_sum_keys(self):
        self.assertEqual(t.sumKeys(t.root.left.left),30)
    def test_disbalances_cost(self):
        self.assertEqual(t.sumDisbalance(t.root), 214)
    
    def test_is_two_balanced(self):
        self.assertEqual(t.isTwoNode(t.root), True)
    def test_is_two_balanced_2(self):
        self.assertEqual(t.isTwoNode(t.root.right.left), True)
    def test_is_two_balanced_3(self):
        self.assertEqual(t.isTwoNode(t.root.left.left), False)
    def test_is_two_balanced(self):
        self.assertEqual(t.isTwoBalanced(t.root.right.left),False)
    def test_count_two_nodes(self):
        self.assertEqual(t.countTwoNodes(t.root),4)
    def test_count_two_nodes_sub(self):
        self.assertEqual(t.countTwoNodes(t.root.right),3)
    
    def test_is_2balanced(self):
        self.assertEqual(t.isTwoBalanced(t.root.right.left), False)
    def test_left_left_right(self):
        self.assertEqual(t.isTwoBalanced(t.root.left.left.right),False)
    def test_sum_keys_2balanced(self):
        self.assertEqual(t.sumKeys2Balanced(t.root), 66)
    # def test_sum_keys_2balanced_root(self):
        # self.assertEqual(t.sumKeys2Balanced(t.root.right), 66)
    

if __name__ == '__main__':
    result = input().split(' ')
    for i,val in enumerate(result):
        input_dict[input_list[i]] = int(val)
    t = Tree(input_dict['RK'],0,input_dict['RSR'])
    t.rndTree(t.root, 4)

    unittest.main()