import re
import random

# Two special values for boundary nodes
PLUS_INF = 99999
MINUS_INF = -99999

# Node class definition: a quadraic node having four links  
class SLnode:
    def __init__(self, key, item):
        self.key = key
        self.item = item
        self.up = None
        self.down = None
        self.next = None
        self.prev = None

    def getKey(self):
        return self.key

    def getItem(self):
        return self.item

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def getUp(self):
        return self.up

    def getDown(self):
        return self.down

    def hasNext(self):
        return (self.next!=None)

    def hasPrev(self):
        return (self.prev!=None)

    def setKey(self, key):
        self.key = key

    def setItem(self, item):
        self.item = item

    def setNext(self, p):
        self.next = p

    def setPrev(self, p):
        self.prev =p
 
    def setUp(self, p):
        self.up = p

    def setDown(self, p):
        self.down = p

# List class definition used in the skip list 
class SLlist:
    def __init__(self):
        self.leftDummy=SLnode(MINUS_INF,"")
        self.rightDummy=SLnode(PLUS_INF,"")
        self.leftDummy.setNext(self.rightDummy)
        self.rightDummy.setPrev(self.leftDummy)
        self.size = 0
        self.insert_cursor = self.getleftDummy()

    def getleftDummy(self):
        return self.leftDummy

    def getrightDummy(self):
        return self.rightDummy

    def getSize(self):
        return self.size

    def increaseSize(self):
        self.size=self.size + 1

    def decreaseSize(self):
        self.size=self.size - 1

    '''
    method insertAfter(self, p, SLnode): insert a node in the list after node p
    '''
    def insertAfter(self, p, SLnode):
        temp = self.getleftDummy()
        ok = 1
        while temp != p:
            temp = temp.getNext()
            if temp == None:
                ok = 0
                break
        if ok == 1:
            t_next = temp.getNext()
            temp.setNext(SLnode)
            t_next.setPrev(SLnode)
            SLnode.setPrev(temp)
            SLnode.setNext(t_next)
            self.increaseSize()

    '''
    method print_List(self): print the content of the list
    '''
    def print_List(self):
        temp = self.getleftDummy()
        while temp != None:
            print("({0},{1})".format(temp.getKey(), temp.getItem()), end="")
            temp = temp.getNext()
        print()

        

# Skip list definition: a list of lists is used
class Skip_Lists:
    def __init__(self):
        self.S=[SLlist()]

    def getLists(self):
        return self.S

    # use the number of nodes in the bottom list to denote the Size
    def getSize(self):
        return self.S[0].getSize()

    # use Height to denote the number of lists used in the skip list
    def getHeight(self):
        return len(self.S)

    def isEmpty(self):
        return ((self.getHeight()==1) and (self.getSize()==0))

    # Derive the top list in the skip list
    def getTopList(self):
        return self.S[self.getHeight()-1]

    '''
    method getTopleft(self): get the topleft node in the skip list
    '''
    # Derive the topleft node in the skip list
    def getTopleft(self):
        return self.getTopList().getleftDummy()
        
    '''
    method addEmptyList(): padding the skip list when the number of copies of the inserted node
    is more than the height of the current skip list
    '''
    def addEmptyList(self):
        top = self.getTopList()
        new = SLlist()
        top.getleftDummy().setUp(new.getleftDummy())
        top.getrightDummy().setUp(new.getrightDummy())
        new.getleftDummy().setDown(top.getleftDummy())
        new.getrightDummy().setDown(top.getrightDummy())
        self.getLists().append(new)
        
    '''
    method search(node): search the skip list with the given node using the key
    '''
    def search(self, node):
        temp = self.getTopleft()
        while temp.hasNext():
            if temp.getNext().getKey() > node.getKey():
                if temp.getDown() == None:
                    break
                temp = temp.getDown()
            elif temp.getNext().getKey() < node.getKey():
                temp = temp.getNext()
            elif temp.getNext().getKey() == node.getKey():
                return temp.getNext()
        return None

    '''
    method delete(node): delete the given node from the skip list
    '''
    def delete(self, node):
        temp = self.search(node)
        if temp == None:
            print("Key not found in the skip lists and will not perform the deletion")
            return
        
        while temp != None:
            temp.getNext().setPrev(temp.getPrev())
            temp.getPrev().setNext(temp.getNext())
            temp = temp.getDown()
        
        temp = self.getTopleft()
        while temp.getDown() != None:
            if temp.getDown().getNext().getKey() == PLUS_INF:
                temp = temp.getDown()
                self.getLists().pop() #remove extra (-99999,)(99999,)
            else:
                break
        
    '''
    method insert(node): insert the given node to the skip list
    '''
    def insert(self, node):
        temp = self.getTopleft()
        # print(temp.getKey(),temp.getItem())
        while temp.hasNext():
            if temp.getNext().getKey() < node.getKey():
                temp = temp.getNext()
            elif temp.getNext().getKey() > node.getKey():
                if temp.getDown() == None:
                    self.getLists()[0].insertAfter(temp,node)
                    break
                else:
                    temp = temp.getDown()
            else:
                print("Key found in the skip lists and will not inert the new node")
                return

        temp = temp.getNext()
        level = coin_tossing()
        # print("level : ", level)
        for i in range(level + 2 - self.getHeight()):
            self.addEmptyList()
        for i in range(1, level + 1):
            temp.setUp(SLnode(node.getKey(), node.getItem()))
            # print(i, temp.getUp().getKey(), temp.getUp().getItem())
            temp.getUp().setDown(temp)
            temp = temp.getUp()
            t_now = self.getLists()[i].getleftDummy()
            while t_now.hasNext():
                if t_now.getNext().getKey() < temp.getKey():
                    t_now = t_now.getNext()
                else:
                    self.getLists()[i].insertAfter(t_now, temp)
                    break

'''
function for coin tossing with the number of heads returned
'''
def coin_tossing():
    if random.randint(0,1):
        return 1 + coin_tossing()
    return 0
    
'''
function for reading lines (entries) in the input text file into a list of strings
'''
def read_lines():
    with open('inFile.txt', "r") as f:
        entryList = [x.strip() for x in f.readlines()]
    f.close()
    return entryList
    
'''
function for starting the task
'''
def create_SkipLists():
    #
    # read the input information from the default input text file into an
    # entry list, entry_list
    #
    entry_list=read_lines()
    #
    # initiating a skip list object SL
    #
    SL=Skip_Lists()
    for index in range(0, len(entry_list)):
        # splitting the string by " " symbol for deriving the entry                                       
        pairs = re.split(" ",entry_list[index])
        # making a new node for the entry
        newnode=SLnode(int(pairs[0]), pairs[1])
        # inserting the new node to the skip list SL
        SL.insert(newnode)

    #--------------dynamic operations with result printed -----------------------------------
    for i in range(0,SL.getHeight()):
        SL.S[i].print_List()

    print("Insert (88, luke)")
    SL.insert(SLnode(88, "luke"))
    for i in range(0,SL.getHeight()):
        SL.S[i].print_List()

    print("delete (40, kite)")
    SL.delete(SLnode(40, "kite"))
    for i in range(0,SL.getHeight()):
        SL.S[i].print_List()

    print("Insert (27, eric)")
    SL.insert(SLnode(27, "eric"))
    for i in range(0,SL.getHeight()):
        SL.S[i].print_List()

    print("delete (45, lisa)")
    SL.delete(SLnode(45, "lisa"))
    for i in range(0,SL.getHeight()):
        SL.S[i].print_List()

    print("delete (27, luis)")
    SL.delete(SLnode(27, "luis"))
    for i in range(0,SL.getHeight()):
        SL.S[i].print_List()

    print("delete (8, kids)")
    SL.delete(SLnode(8, "kids"))
    for i in range(0,SL.getHeight()):
        SL.S[i].print_List()

    print("delete (88, luke)")
    SL.delete(SLnode(88, "luke"))
    for i in range(0,SL.getHeight()):
        SL.S[i].print_List()

    return

print(read_lines())
print('-----------------------------------------------')
create_SkipLists()