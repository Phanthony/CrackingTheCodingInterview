from LinkedList import *
"""
Palindrome:
Implement a function to check if a linked list is a palindrome
"""

class TestCase():
    
    def tester(self, num, res):
        if res:
            testResult = "passed"
        else:
            testResult = "failed"
        print("Test Case {} {}".format(num,testResult))
        
    def test1(self):
        
        llist = LinkedList()
        llist.append(0)
        llist.append(5)
        llist.append(1)
        llist.append(1)
        llist.append(0)
        
        res = pal(llist)
        
        expected = True
        
        self.tester(1,res==expected)
    
    def test2(self):
        
        llist = LinkedList()
        llist.append(0)
        llist.append(5)
        llist.append(1)
        llist.append(1)
        llist.append(0)
        llist.append(1)
        
        res = pal(llist)
        
        expected = False
        
        self.tester(2,res==expected)    
        
    def runTest(self):
        self.test1()
        self.test2()
        
        

def pal(linkedList):
    """
    Check the lngths of the linkedLists and keep a dictioanry of the data seen
    """
    
    lenCounter = 0
    dataDictionary = {}
    current = linkedList.head
    
    while current != None:
        lenCounter += 1
        count = dataDictionary.get(current.data,0)
        dataDictionary[current.data] = count+1
        current = current.next
        
    if lenCounter%2 == 0:
        for key in dataDictionary:
            if dataDictionary[key]%2 != 0:
                return False
        return True
    else:
        odd = False
        for key in dataDictionary:
            if dataDictionary[key]%2 != 0:
                if odd:
                    return False
                else:
                    odd = True
        return True
        
        
    
    
r = TestCase()
r.runTest()