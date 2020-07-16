"""
Palindrome Permutation:
Given a string, write a function to check if it is a permutation of a palindrome.
A Palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters. The palindrome does not need to be limited
to just dictionary words.
"""

class testCase:
    
    def tester(self, num, res):
        if res:
            testResult = "passed"
        else:
            testResult = "failed"
        print("Test Case {} {}".format(num,testResult))
    
    def test1(self):
        
        string = "tact cao"
        
        res = palPerm(string)
        expected = True
        
        self.tester(1, expected == res)
    
    def test2(self):
        
        string = "act act"
        
        res = palPerm(string)
        expected = True
        
        self.tester(2, expected == res)
        
    def test3(self):
        
        string = "100"
        
        res = palPerm(string)
        expected = True
        
        self.tester(3, expected == res)
        
    def test4(self):
        
        string = "dfasdg"
        
        res = palPerm(string)
        expected = False
        
        self.tester(4, expected == res)
        
    def test5(self):
        
        string = "!()"
        
        res = palPerm(string)
        expected = False
        
        self.tester(5, expected==res)
        
    def test6(self):
        
        string = " a   "
        
        res = palPerm(string)
        expected = True
        
        self.tester(6,expected==res)
        
    def runtests(self):
        self.test1()
        self.test2()
        self.test3()
        self.test4()
        self.test5()
        self.test6()
        
def palPerm(string):
    #remove spaces from the string
    #check length of string
    #if length of string is even - all characters have to have an even amount
    #if length of string is odd - all but 1 character needs to have even amounts
    #using a dict keep a counter of the character count
    
    strippedString = string.replace(" ","")
    charCount = {}
    for char in strippedString:
        count = charCount.get(char,0)
        charCount[char] = count+1
    if len(strippedString)%2 == 0:
        for key in charCount:
            if charCount[key]%2 != 0:
                return False
        return True
    else:
        oddCount = False
        for key in charCount:
            if charCount[key]%2 != 0:
                if oddCount:
                    return False
                else:
                    oddCount = True
        return True
    
r = testCase()
r.runtests()