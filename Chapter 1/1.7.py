"""
Rotate Matrix:
Given an image represented by an NxN matrix, where each pixel is 4 bytes
write a method to rotate the image by 90 degrees. Try doing this in place
"""


"""
[a,b,c]
[x,y,z]
[p,q,r]

[p,x,a]
[q,y,b]
[r,z,c]

"""

"""
[a,b,c,m]
[d,e,f,n]
[g,h,i,o]
[j,k,l,p]

[j,g,d,a]
[k,h,e,b]
[l,i,f,c]
[p,o,n,m]

"""

"""
[01,02,03,04,05]
[06,07,08,09,10]
[11,12,13,14,15]
[16,17,18,19,20]
[21,22,23,24,25]

[21,16,11,06,01]
[22,17,12,07,02]
[23,18,13,08,03]
[24,19,14,09,04]
[25,20,15,10,05]
"""

"""
N = 7
L0: Start 0 End 5
L1: Start 1 End 4
L2: Start 2 End 3
[0 * * * * * 0]
[* 1 * * * 1 *]
[* * 2 * 2 * *]
[* * * 3 * * *]
[* * 2 * 2 * *]
[* 1 * * * 1 *]
[0 * * * * * 0]


N = 6
L0: Start 0 End at 4
L1: Start 1 End at 3
L2: Start 2 End at 2
[0 * * * * 0]
[* 1 * * 1 *]
[* * 2 2 * *]
[* * 2 2 * *]
[* 1 * * 1 *]
[0 * * * * 0]

N = 5
L0: Start 0 End 3
L1: Start 1 End 2
[0 * * * 0]
[* 1 * 1 *]
[* * 2 * *]
[* 1 * 1 *]
[0 * * * 0]
"""



class testCase():
    
    def tester(self, num, res):
        if res:
            testResult = "passed"
        else:
            testResult = "failed"
        print("Test Case {} {}".format(num,testResult))
        
    def test1(self):
        
        matrix = [["a","b","c"],["x","y","z"],["p","q","r"]]
        
        res = rotMat(matrix)
        expected = [["p","x","a"],["q","y","b"],["r","z","c"]]
        
        self.tester(1,res==expected)
        
    def test2(self):
        
        matrix = [["a","b","c","m"],["d","e","f","n"],["g","h","i","o"],["j","k","l","p"]]
        
        res = rotMat(matrix)
        expected = [["j","g","d","a"],["k","h","e","b"],["l","i","f","c"],["p","o","n","m"]]
        
        self.tester(2,res==expected)
        
    def test3(self):
        
        matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
        
        res = rotMat(matrix)
        expected = [[21,16,11,6,1],[22,17,12,7,2],[23,18,13,8,3],[24,19,14,9,4],[25,20,15,10,5]]
        
        self.tester(3,res==expected)
    
    def runTest(self):
        self.test1()
        self.test2()
        self.test3()
        
def rotMat(matrix):
    """
    n is length of matrix
    for some byte to get the new row index - based on old column index
    for some byte to get the new column index - based on function (N - 1) - old row index
    """
    print()
    for row in matrix:
        print(row)
    print()
    for layer in range(0,len(matrix)//2):
        end = len(matrix)-1-layer
        col = layer
        while col < end:
            current = matrix[layer][col]
            oldRow = layer
            oldCol = col
            for i in range(0,5):
                newRow = oldCol
                newCol = len(matrix) - oldRow - 1
                temp = matrix[newRow][newCol]
                matrix[newRow][newCol] = current
                current = temp
                oldRow = newRow
                oldCol = newCol
            col += 1
        print("Current Layer: {}".format(layer))
        for row in matrix:
            print(row)
        print()        
    return matrix

        
r = testCase()
r.runTest()