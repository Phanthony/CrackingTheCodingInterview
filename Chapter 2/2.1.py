from LinkedList import *

"""
Remove Dups:
Write a method to remove duplicates from an unsorted linked list
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
        
        expected = LinkedList()
        expected.append(1)
        expected.append(5)
        expected.append(10)
        expected.append(3)
        expected.append(4)
        
        res = removeDup(llist)
        
        self.tester(1,testLists(res,expected))
        
    def test2(self):
        
        llist = LinkedList()
        llist.append(1)
        llist.append(1)
        
        expected = LinkedList()
        expected.append(1)
        
        res = removeDup(llist)
        
        self.tester(2, testLists(res,expected))
    
    def runTest(self):
        self.test1()
        self.test2()
        
def testLists(l1,l2):
    c1 = l1.head
    c2 = l2.head
    while c1 != None:
        if c1.data != c2.data:
            return false
        c1 = c1.next
        c2 = c2.next
    return True
        
def removeDup(linkedList):
    """ 
    use a dictionary to remember what data entries have already been seen
    while looping through the linked list
    """
    seen = {}
    
    curr = linkedList.head
    prev = None
    if curr == None:
        return linkedList
    while curr.next != None:
        count = seen.get(curr.data,0)
        if count == 0:
            seen[curr.data] = 1
            prev = curr
        else:
            temp = curr.next
            prev.next = temp
        curr = curr.next
        
    count = seen.get(curr.data,0)
    if count != 0:
        prev.next = None
    return linkedList
    
r = TestCase()
r.runTest()
    
    
    