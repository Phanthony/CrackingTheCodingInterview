"""
URLify:
Write a method to replace all spaces in  astring with %20
You may assume that the string has sufficient space at the end to hold the additional characters
and that you are given the true length of the string. Operation has to be done in place
"""

class testCase:
    
    def tester(self, num, res):
        if res:
            testResult = "passed"
        else:
            testResult = "failed"
        print("Test Case {} {}".format(num,testResult))
        
    def test1(self):
        
        string = "Mr John Smith    "
        length = 13
        
        res = url(string, length)
        expected = "Mr%20John%20Smith"
        
        self.tester(1,expected==res)
        
    def test2(self):
        
        string = "FireAlarm"
        length = 9
        
        res = url(string, length)
        expected = "FireAlarm"
        
        self.tester(2,expected==res)
        
    def test3(self):
        
        string = "         "
        length = 3
        
        res = url(string, length)
        expected = "%20%20%20"
        
        self.tester(3,expected==res)
        
    def test4(self):
        
        string = " trees     "
        length = 7
        
        res = url(string, length)
        expected = "%20trees%20"
        
        self.tester(4,expected==res)
    
    def test5(self):
        
        string = ""
        length = 0
        
        res = url(string, length)
        expected = ""
        
        self.tester(5, expected==res)
    
    def test6(self):
        
        string = "   "
        length = 1
        
        res = url(string, length)
        expected = "%20"
        
        self.tester(6, expected==res)
        
    def runTest(self):
        self.test1()
        self.test2()
        self.test3()
        self.test4()
        self.test5()
        self.test6()    
        

def url(string,length):
    #working from the end of the string, build the urlified string
    
    # Since strings a immutable in python, convert to a list first
    
    if length == 0:
        return string
    
    buildPos = len(string)-1
    stringPos = length-1
    
    listString = list(string)
    while stringPos >= 0:
        if listString[stringPos] == " ":
            listString[buildPos] = "0"
            listString[buildPos-1] = "2"
            listString[buildPos-2] = "%"
            buildPos -=3
        else:
            listString[buildPos] = listString[stringPos]
            buildPos -=1
        stringPos -=1
    
    string = ''.join(listString)
            
    return string

r = testCase()
r.runTest()
