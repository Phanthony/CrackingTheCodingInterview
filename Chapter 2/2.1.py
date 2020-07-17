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
        
        self.tester(1,expected==llist)
        
    def runTest(self):
        self.test1()
        
def removeDup(linkedList):
    """ 
    use a dictionary to remember what data entries have already been seen
    while looping through the linked list
    """
    print(linkedList)
    seen = {}
    
    curr = linkedList.head
    prev = None
    if curr == None:
        return linkedList
    while curr.next != None:
        count = seen.get(curr.data,0)
        if count == 0:
            seen[curr.data] = 1
        else:
            temp = curr.next
            prev.next = temp
        prev = curr
        curr = curr.next
    """   
    count = seen.get(curr.data,0)
    if count != 0:
        prev.next = None
    """
    print(linkedList)
r = TestCase()
r.runTest()
    
    
    