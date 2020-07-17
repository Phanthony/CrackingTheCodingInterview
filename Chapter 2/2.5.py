from LinkedList import *
"""
Sum List:
You have two numbers represnted by a linked list where each node contains a single digit. 
The digits are stored in reverse order, such that the 1's digit is at the head of the list.
Write a function that adds the two numbers and retruns the sum as a linked list.
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
        
        llist2 = LinkedList()
        llist2.append(5)
        llist2.append(5)
        
        llist3 = LinkedList()
        llist3.append(5)
        llist3.append(0)
        llist3.append(2)
        
        res = sumList(llist,llist2)
        print(res)
        print(llist3)
        
        self.tester(1,llist3==res)
    
    def runTest(self):
        
        self.test1()
        

def sumList(list1,list2):
    """
    build the numbers as you go through the linked lists
    """
    
    num1 = 0
    pos1 = 1
    pointer1 = list1.head
    while pointer1 != None:
        num1 += pointer1.data * pos1
        pos1 *= 10
        pointer1 = pointer1.next
        
    num2 = 0
    pos2 = 1
    pointer2 = list2.head
    while pointer2 != None:
        num2 += pointer2.data * pos2
        pos2 *= 10
        pointer2 = pointer2.next
        
    res = num2 + num1
    
    resList = LinkedList()
    
    
    while res != 0:
        resList.append(res%10)
        res = res//10
    
    return resList

r = TestCase()
r.runTest()