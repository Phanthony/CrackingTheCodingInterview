"""
One Away:
There are 3 types of edits that can be performed on strings:
Insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit or ero edits away.
"""

class testCase():
    
    def tester(self, num, res):
        if res:
            testResult = "passed"
        else:
            testResult = "failed"
        print("Test Case {} {}".format(num,testResult))
        
    def test1(self):
        
        string1 = "pale"
        string2 = "ple"
        
        res = oneAway(string1,string2)
        expected = True
        
        self.tester(1, expected==res)
        
    def test2(self):
        
        string1 = "pales"
        string2 = "pale"
        
        res = oneAway(string1,string2)
        expected = True
        
        self.tester(2, expected==res)
        
            
    def test3(self):
        
        string1 = "pale"
        string2 = "bale"
        
        res = oneAway(string1,string2)
        expected = True
        
        self.tester(3, expected==res)
        
    def test4(self):
        
        string1 = "pale"
        string2 = "bake"
        
        res = oneAway(string1,string2)
        expected = False
        
        self.tester(4, expected==res)
        
    def test5(self):
        
        string1 = "pale"
        string2 = "pales"
        
        res = oneAway(string1,string2)
        expected = True
        
        self.tester(5, expected==res)    
                                
    def runtests(self):
        self.test1()
        self.test2()
        self.test3()
        self.test4()
        self.test5()
    

def oneAway(string1,string2):
    """
    Check the lenghts of the strings to see if 
    the difference is 1.
    If lengths are same, compare each character
    If lengths are different:
    Use two pointers for strings moving through them and checking the characters
    Check the shorter string against the longer string
    """
    
    if abs(len(string1)-len(string2)) > 1:
        return False
    
    if len(string1) == len(string2):
        difference = False
        for i,char in enumerate(string1):
            if char != string2[i]:
                if difference:
                    return False
                difference = True
        return True
    
    maxCheck = min(len(string1),len(string2))
    
    stringList = [string1,string2]
    
    smaller = 0
    bigger = 1
    if len(string1) > len(string2):
        smaller = 1
        bigger = 0
        
    pointer1 = 0
    pointer2 = 0
    
    difference = False
    while pointer1 < maxCheck:
        if stringList[smaller][pointer1] != stringList[bigger][pointer2]:
            if difference:
                return False
            difference = True
            pointer2 += 1
        else:
            pointer1 += 1
            pointer2 += 1
    return True
    
r = testCase()
r.runtests()
            