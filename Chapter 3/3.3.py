import math
"""
Stack of Plates:
Design an stack class that has a cap on the amount of elements in it.
When it reachs the cap, create a new stack to add elements in. Should have
push and pop that behave exactly in the same way as if it was a regular stack.
"""

class SetOfStacks:
    
    def __init__(self,stackLimit = 3):
        self.stackLimit = stackLimit
        currentStack = None
        self.stackHolder = []
        
    def push(self, element):
        if self.currentStack == None:
            newStack = [element]
            self.stackHolder.add(newStack)
        else:
            if len(self.stackHolder[self.currentStack]) == self.stackLimit - 1:
                self.currentStack += 1
                newStack = [element]
                self.stackHolder.add(newStack)
            else:
                self.stackHolder[self.currentStack].add(element)
    def pop(self):
        if self.currentStack == None:
            self.currentStack = None
            return None
        
        if len(self.stackHolder[self.currentStack]) == 1:
            temp = self.stackHolder[self.currentStack][0]
            self.stackHolder = self.stackHolder[:-1]
            self.currentStack -=1
            return temp
        else:
            return self.stackHolder[self.currentStack].pop()
        
    def popAt(self, index):
        stackPos = ceil(popAt/(self.stackLimit))
        if self.currentStack == None:
            self.currentStack = None
            return None
        
        if len(self.stackHolder[stackPos]) == 1:
            temp = self.stackHolder[self.currentStack][0]
            self.stackHolder = self.stackHolder[:-1]
            self.currentStack -=1
            return temp
        else:
            return self.stackHolder[self.currentStack].pop()        