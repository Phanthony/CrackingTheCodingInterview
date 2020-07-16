"""
Is Unique:
Implement an algorithm to determine if a string has all unique characters. 
What if you can't use additional data structures?
"""

def isUnique(string):
    #Use a dictionary to map number of times we've seen each character occurance. If more than 1 then return false
    charCheck = {}
    for char in string:
        if charCheck.get(char, 0) == 0:
            charCheck[char] = 1
        else:
            return False
    return True

class testCase:
    
    
    
    def tester(self, num, res):
        if res:
            testResult = "passed"
        else:
            testResult = "failed"
        print("Test Case {} {}".format(num,testResult))
    
    def test1(self):
        
        string = "abcdefghijklmnopqrstuvwxyz"
        res = isUnique(string)
        expected = True
        
        self.tester(1,res==expected)
        
    def test2(self):
        
        string = "ijijincvf"
        res = isUnique(string)
        expected = False
        
        self.tester(1,res==expected)
        
    def test3(self):
        
        string = "huomcfaa"
        res = isUnique(string)
        expected = False
        
        self.tester(3,res==expected)
        
    def test4(self):
        
        string = "1235432"
        res = isUnique(string)
        expected = False
        
        self.tester(4,res==expected)
    
    def test5(self):
        
        string = "!@#$^%,./"
        res = isUnique(string)
        expected = True
        
        self.tester(5,res==expected)
        
    def runTest(self):
        self.test1()
        self.test2()
        self.test3()
        self.test4()
        self.test5()
    
r = testCase()
r.runTest()
    

