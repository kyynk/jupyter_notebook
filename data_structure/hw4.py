import re
# Node class 
# Note: item will not be used here and will use key only
class Node:
    def __init__(self, key, item):
        self.key = key
        self.item = item
        self.parent = None
        self.right = None
        self.left = None
    
    def getKey(self):
        return self.key

    # may not be used
    def getItem(self):
        return self.item
        
    def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left
        
    def getParent(self):
        return self.parent

    def hasRightChild(self):
        return self.right != None

    def hasLeftChild(self):
        return self.left != None

    def isRoot(self):
        return self.parent == None

    def isLeaf(self):
        return self.right == None and self.left == None

    def isRightChild(self):
        return self.parent.getRightChild() == self
    
    def isLeftChild(self):
        return self.parent.getleftChild() == self

    def setParent(self, p):
        self.parent = p

    def setKey(self, key):
        self.key = key

    # may not be used
    def setItem(self, item):
        self.item = item
        
    def addRightChild(self, n):
        self.right = n

    def addLeftChild(self, n):
        self.left = n

# Binary Tree class 
class BinaryTree:
    def __init__(self):
        self.root = None
        self.pos = None
        self.size = 0

    def isEmpty(self):
        return self.root == None

    def getSize(self):
        if self.isEmpty():
            return 0
        else:
            return self.getLeftChild().getSize() + 1 + self.getRightChild().getSize()

    def getRoot(self):
        return self.root

    def getPosition(self):
        return self.pos

    def setRoot(self, node):
        self.root = node

    def setPosition(self, node):
        self.root = node
    
    # locate the node with the key, where the "node" parameter is the staring node for locating process
    def findPosition(self, node, key): # assume node is root
        if node != None:
            if node.getKey() == key:
                return node
            else:
                l = self.findPosition(node.getLeftChild(),key)
                r = self.findPosition(node.getRightChild(),key)
                if l != None:
                    return l
                if r != None:
                    return r
        return None

    #
    # For management, print the binary tree in pre-order
    #
    def printBinaryTreeinPreOrder(self, node):
        if node != None:
            if node.getKey() != '-':
                print(node.getKey(),end='')
                self.printBinaryTreeinPreOrder(node.getLeftChild())
                self.printBinaryTreeinPreOrder(node.getRightChild())
    
# function for reading lines (entries) in the input text file into a list of strings     
def readLines():
    with open('inFileA2.txt', "r+") as f:
        entryListA = [x.strip() for x in f.readlines()]
    f.close()
    with open('inFileB2.txt', "r+") as f:
        entryListB = [x.strip() for x in f.readlines()]
    f.close()
    
    return entryListA, entryListB

# function for building the binary tree
def constructingBinaryTree(entryList):
    #
    # read the input information from the default input text file into an
    # entry list, entryList
    #
    # initiating a binary tree b and return it after the consruction
    #
    b=BinaryTree()
    n = Node(entryList[0][0], None)
    b.setRoot(n)
    for i in range(len(entryList)):
        for j in range(0,len(entryList[i]),2):
            temp = Node(entryList[i][j], None)
            if j == 0:
                ss = b.findPosition(b.getRoot(), entryList[i][j])
            if j == 2:
                ss.addLeftChild(temp)
            if j == 4:
                ss.addRightChild(temp)
    return b

#
# bt1 and bt2 stand for the given binary tree 1 and 2
# The input will be the (same) nodes located at these two trees respectively for comparison
#
def check(n1, n2):
    if n1.hasLeftChild() and not n1.hasRightChild():
        if not n2.hasLeftChild() and n2.hasRightChild():
            return True
    if not n1.hasLeftChild() and n1.hasRightChild():
        if n2.hasLeftChild() and not n2.hasRightChild():
            return True
    if n1.hasLeftChild() and n1.hasRightChild():
        if n1.getLeftChild().getKey() == n2.getRightChild().getKey():
            return True
        if n1.getRightChild().getKey() == n2.getLeftChild().getKey():
            return True
    return False

def deriveTheDistance(bt1Node, bt2Node):
    # print('wat')
    if bt1Node == None and bt2Node == None:
        return 0
    if check(bt1Node, bt2Node):
        # print('the')
        return 1 + deriveTheDistance(bt1Node.getLeftChild(), bt2Node.getRightChild()) + deriveTheDistance(bt1Node.getRightChild(), bt2Node.getLeftChild())
    else:
        # print('hel')
        return deriveTheDistance(bt1Node.getLeftChild(), bt2Node.getLeftChild()) + deriveTheDistance(bt1Node.getRightChild(), bt2Node.getRightChild())
        
entryList1, entryList2 = readLines()
bt1=constructingBinaryTree(entryList1)
bt2=constructingBinaryTree(entryList2)
print("preorder of tree 1: ", end='')
bt1.printBinaryTreeinPreOrder(bt1.getRoot())
print()
print("preorder of tree 2: ", end='')
bt2.printBinaryTreeinPreOrder(bt2.getRoot())
print()
print("The distance between two isomorphic binary trees is", deriveTheDistance(bt1.getRoot(), bt2.getRoot()))
#print("The distance between two isomorphic binary trees is", deriveTheDistance(bt2.getRoot(), bt1.getRoot()))