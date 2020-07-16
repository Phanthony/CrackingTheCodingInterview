"""
Check Permutation:
Given two strings, write a method to decide if one is a permutation
of the other
"""

class testCase:
    
    def tester(self, num, res):
        if res:
            testResult = "passed"
        else:
            testResult = "failed"
        print("Test Case {} {}".format(num,testResult))
    
    def test1(self):
        
        string1 = "cat"
        string2 = "act"
        res = checkPermutation(string1,string2)
        expected = True
        
        self.tester(1,res==expected)
        
    def test2(self):
        
        string1 = "808"
        string2 = "080"
        res = checkPermutation(string1,string2)
        expected = False
        
        self.tester(1,res==expected)
        
    def test3(self):
        
        string1 = "Lighter Fluid"
        string2 = "LighterFluid"
        res = checkPermutation(string1, string2)
        expected = False
        
        self.tester(3,res==expected)
        
    def test4(self):
        
        string1 = "12345"
        string2 = "54321"
        res = checkPermutation(string1,string2)
        expected = True
        
        self.tester(4,res==expected)
    
    def test5(self):
        
        string1 = "!!!"
        string2 = "!!!"
        res = checkPermutation(string1,string2)
        expected = True
        
        self.tester(5,res==expected)
        
    def test6(self):
        
        string1 = "!!!!"
        string2 = "!!! "
        res = checkPermutation(string1,string2)
        expected = False
        
        self.tester(6,res==expected)    
        
    def runTest(self):
        self.test1()
        self.test2()
        self.test3()
        self.test4()
        self.test5()
        self.test6()
    
def checkPermutation(string1,string2):
    #Using a dictionary add all characters from string1
    #Afterwards using the dict reduce the char count from characters in str2
    #Check dict for any left over characters not reduced to 0
    if len(string2) != len(string1):
        return False
    
    charChecker = {}
    
    for char1 in string1:
        count = charChecker.get(char1,0)
        charChecker[char1] = count+1
        
    for char2 in string2:
        if charChecker.get(char2,0) == 0:
            return False
        else:
            count = charChecker[char2]
            if count-1 < 0:
                return False
            else: 
                charChecker[char2] = count-1
                
    for key in charChecker:
        if charChecker[key] > 0:
            return False
        
    return True
    
r = testCase()
r.runTest()
