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
        
        self.tester(1, expeceted == res)
        
    def test2():
        