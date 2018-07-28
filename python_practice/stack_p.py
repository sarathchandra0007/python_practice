"""
Stack()
push(item)
pop()
peek()
isEmpty()
size()
"""

class stack(object):
    def __init__(self):
        self.arr=[]
        
    def push(self,data):
            self.arr.append(data)
    def isEmpty(self):
        return self.arr==[]
    def pop(self):
        return self.arr.pop()
    def peek(self):
        return self.arr[-1]
    def printstack(self):
        print (self.arr)


    def balance_check(self,s):
        for i in s:
            if i in set('[({'):
                self.push(i)
                self.printstack()
            else:
                self.pop()

        if self.arr==[]:
            return True
        else:
            return False

s=stack()
print (s.balance_check('[](){([[[]])}'))

