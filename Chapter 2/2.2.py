from LinkedList import *
"""
Return the Kth to last:
Implement an algorithm to find the kth to last element of a singly linked list
If the list is shorter than K then return the last element
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
        llist.append(1)
        llist.append(5)
        llist.append(10)
        llist.append(3)
        llist.append(5)
        llist.append(3)
        llist.append(4)
        llist.append(3)
        
        expected = 4
        
        res = kLast(llist,1)
        
        self.tester(1,expected==res)
        
    def test2(self):
        
        llist = LinkedList()
        llist.append(1)
        llist.append(5)
        llist.append(10)
        llist.append(3)
        llist.append(5)
        llist.append(3)
        llist.append(4)
        llist.append(3)
        
        expected = 3
        
        res = kLast(llist,0)
        
        self.tester(2,expected==res)
        
    def test3(self):
        
        llist = LinkedList()
        llist.append(1)
        llist.append(5)
        llist.append(10)
        llist.append(3)
        llist.append(5)
        llist.append(3)
        llist.append(4)
        llist.append(3)
        
        expected = 3
        
        res = kLast(llist,4)
        
        self.tester(3,expected==res)
        
    def test4(self):
        
        llist = LinkedList()
        llist.append(1)
        llist.append(5)
        
        expected = 5
        
        res = kLast(llist,4)
        
        self.tester(4,expected==res)      
        
    def runTest(self):
        self.test1()
        self.test2()
        self.test3()
        self.test4()
        
def kLast(linkedList, k):
    """
    using two points to create a sliding window, go ahead k elements with the 2nd pointer
    After that you increment both pointers until the 2nd pointer hits the end of the list
    return the item on the 1st pointer
    """
    
    if linkedList.head == None:
        return None
    
    p1 = linkedList.head
    p2 = linkedList.head
    
    i = 0
    while (i < k) and (p2.next != None):
        p2 = p2.next
        i += 1
        
    if i != k:
        return p2.data
    
    while p2.next != None:
        p1 = p1.next
        p2 = p2.next
    
    return p1.data


r = TestCase()
r.runTest()