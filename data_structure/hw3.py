'''# Queue class: can be implemented using a list in Python
class Queue:
    def __init__(self):
        self.queue = []
    #enqueue()
    def enqueue(self, item):
        self.queue.append(item)
    #dequeue()
    def dequeue(self):
        temp = self.queue[0]
        self.queue = self.queue[1:]
        return temp
    def isEmpty(self):
        if self.queue == []:
            return True
        return False
    def size(self):
        return len(self.queue)
    def front(self):
        return self.queue[0]

# function for generating all the binary numbers smaller than or equal to a given number n
def generateBinaryNumbers(n):
    q = Queue()
    q.enqueue("1")
    binaryNum = []
    while(n > 0):
        n-=1
        s = q.front()
        binaryNum.append(q.dequeue())
        q.enqueue(s+"0")
        q.enqueue(s+"1")
    return binaryNum

n=10
print("When n is,",n,", the binary numbers are:")
print(generateBinaryNumbers(n))

n=13
print("When n is,",n,", the binary numbers are:")
print(generateBinaryNumbers(n))'''
import sys

# Node class 
class Node:
    def __init__(self):
        self.data = -(sys.maxsize-1)
        self.next = None

    # get the data in this node
    def getData(self):
        return self.data

    # get the next node
    def getNext(self):
        return self.next

    # set the data (an integer) to this node
    def setData(self, i):
        self.data = i

    # assign the next node to this node 
    def setNext(self, newNext):
        self.next = newNext

# Define the class of the linked list class
class linkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    # methods for managing the list
    def isEmpty(self):
        return self.head == None

    def size(self):
        length = 0
        current = self.head
        while current != None:
            length += 1
            current = current.getNext()
        return length

    def isHead(self, node):
        return self.head == node

    def isTail(self, node):
        return self.tail == node
    
    # get the head of the list
    def getHead(self):
        return self.head

    # get the tail of the list
    def getTail(self):
        return self.tail

    # set the head of the list
    def setHead(self, node):
        self.head = node

    # set the tail of the list
    def setTail(self, node):
        self.tail = node

    # insert a new node n after node p
    def insertAfter(self, p, n):
        current = self.getHead()
        while current != None:
            if current == p:
                n.setNext(current.getNext())
                current.setNext(n)
                break
            current = current.getNext()

    # insert a new node at head
    def insertAtHead(self, n): 
        n.setNext(self.getHead())
        self.setHead(n)

    # insert a new node at tail
    def insertAtTail(self, n):
        self.getTail().setNext(n)
        self.setTail(n)

    # delete a node at head
    def deleteAtHead(self):
        temp = self.getHead()
        self.setHead(self.getHead().getNext())
        return temp

    # This is used to print the Linked list
    def printLinkedList(self):
        current = self.getHead()
        while current != self.getTail():
            print("[ %d ]-->" %current.getData(),end='')
            current = current.getNext()
        print("[ %d ]" %current.getData())


# function readInputListintoLinkedList()
def readInputListintoLinkedList(A):
    LA = linkedList()
    t = Node()
    t.setData(A[0])
    LA.setHead(t)
    LA.setTail(t)
    p = LA.getTail()
    #print(LA.getHead().getData(),LA.getTail().getData())
    for i in range(1,len(A)):
        tt = Node()
        tt.setData(A[i])
        LA.setTail(tt)
        p.setNext(tt)
        p = p.getNext()
        #print(LA.getHead().getData(),LA.getTail().getData())
    return LA


# function mergeLinkedLists()
def mergeLinkedLists(A,B):
    n = A.size()
    while n > 0:
        n -= 1
        tA = A.getHead()
        tB = B.getHead()
        while tA != None and tB != None:
            if tA.getData() > tB.getData():
                temp = tA.getData()
                tA.setData(tB.getData())
                tB.setData(temp)
                tB = tB.getNext()
            tA = tA.getNext()
    return [A,B]



#A=[2, 4, 7, 9, 10]
#B=[1, 3, 5, 8]
A=[4, 8, 12, 17, 20, 27, 33]
B=[1, 6, 9, 18, 25, 30, 45, 66, 77]
LA=readInputListintoLinkedList(A)
LB=readInputListintoLinkedList(B)
print("The input sorted linked lists:")
print("A:", end="")
LA.printLinkedList()
print("B:", end="")
LB.printLinkedList()

[LA, LB]=mergeLinkedLists(LA, LB)
print("The merged sorted linked lists:")
print("A:", end="")
LA.printLinkedList()
print("B:", end="")
LB.printLinkedList()