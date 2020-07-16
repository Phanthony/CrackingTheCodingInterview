"""
String Compression:
Implement a method to perform basic string compression using the counts of repeated characters.
If the compressed string would not become smaller than the original string, return the original string.
Safe to assume the string only has uppercase and lowercase letters
Assuming that lowercase letters are different from uppercase letters
"""

class testCase():
    
    def tester(self, num, res):
        if res:
            testResult = "passed"
        else:
            testResult = "failed"
        print("Test Case {} {}".format(num,testResult))
    
    def test1(self):
        
        string = "aabcccccaaa"
        
        res = stringComp(string)
        expected = "a2b1c5a3"
        
        self.tester(1,expected==res)
    
    def test2(self):
        
        string = "aa"
        
        res = stringComp(string)
        expected = "aa"
        
        self.tester(2,expected==res)
    
    def test3(self):
        
        string = "aaAAbBBcccc"
        
        res = stringComp(string)
        expected = "a2A2b1B2c4"
        
        self.tester(3,expected==res)
    
    def test4(self):
        
        string = ""
        
        res = stringComp(string)
        expected = ""
        
        self.tester(4,expected==res)
        
    def test5(self):
        
        string = "c"
        
        res = stringComp(string)
        expected = "c"
        
        self.tester(5,expected==res)
    
    def runTest(self):
        self.test1()
        self.test2()
        self.test3()
        self.test4()
        self.test5()
        
def stringComp(string):
    """
    go through each character of the string keeping a counter of repeating characters in order
    compare lengths of the string to compression
    """
    
    if len(string)<2:
        return string
    
    occuranceList = []
    
    currentChar = string[0]
    seen = 1
    for char in string[1:]:
        if currentChar == char:
            seen += 1
        else:
            occuranceList.append((currentChar,seen))
            seen = 1
            currentChar = char
            
    occuranceList.append((currentChar,seen))
    
    compString = ""
    
    for char,times in occuranceList:
        compString += (char + str(times))
    
    if len(compString) < len(string):
        return compString
    else:
        return string
    
r = testCase()
r.runTest()