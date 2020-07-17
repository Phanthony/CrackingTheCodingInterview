"""
Zero Matrix:
Write an algorithm such that if an element in an MxN matrix is 0, the entire row and column is set to 0
"""

class testCase():
    
    def tester(self, num, res):
        if res:
            testResult = "passed"
        else:
            testResult = "failed"
        print("Test Case {} {}".format(num,testResult))

    
    def test1(self):
        """
        [1 2 3]
        [0 2 1]
        
        [0 2 3]
        [0 0 0]
        """
        
        matrix = [[1,2,3],[0,2,1]]
        
        res = zeroM(matrix)
        expected = [[0,2,3],[0,0,0]]
        
        self.tester(1,expected==res)
        
    def test2(self):
        """
        [1 2 3 9]
        [0 2 1 2]
        [9 2 3 3]
        [0 3 5 1]
        [8 3 1 0]
        
        [0 2 3 0]
        [0 0 0 0]
        [0 2 3 0]
        [0 0 0 0]
        [0 0 0 0]
        """
        
        matrix = [[1,2,3,9],[0,2,1,2],[9,2,3,3],[0,3,5,1],[8,3,1,0]]
        
        res = zeroM(matrix)
        expected = [[0,2,3,0],[0,0,0,0],[0,2,3,0],[0,0,0,0],[0,0,0,0]]
        
        self.tester(2,expected==res)        
        
    def runTest(self):
        self.test1()
        self.test2()
        
def zeroM(matrix):
    """
    for each row of the matrix find all zero's then set the whole row to 0 if there is one
    go through each column and set them to 0's based on saved zero's positions from rows
    """
    
    zeroList = set()
    zeroRows = set()
    
    for rIndex, row in enumerate(matrix):
        setZero = False
        found = None
        for cIndex, num in enumerate(row):
            if setZero:
                if num == 0:
                    zeroList.add(cIndex)
                row[cIndex] = 0
            elif num == 0:
                zeroList.add(cIndex)
                setZero = True
                found = cIndex
                row[cIndex] = 0
        if setZero:
            for i in range(0, found):
                row[i] = 0
            zeroRows.add(rIndex)
    for colNum in zeroList:
        for rowNum in range(0,len(matrix)-1):
            if rowNum not in zeroRows:
                matrix[rowNum][colNum] = 0
                
    for row in matrix:
        print(row)
    return matrix
    
r = testCase()
r.runTest()
        
        
            