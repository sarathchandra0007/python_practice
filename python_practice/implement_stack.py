"""
Stack()
push(item)
pop()
peek()
isEmpty()
size()
"""

class stack(object):
    def __init__(self,size):
        self.size=size
        self.arr=[]
        
    def push(self,data):
        if self.size>len(self.arr):
            self.arr.append(data)
        else:
            print ("stack overflow")
    def isEmpty(self):
        return self.arr==[]
    def pop(self):
        return self.arr.pop()
    def peek(self):
        return self.arr[-1]
    def printstack(self):
        print (self.arr)

s=stack(2)
s.push(5)
s.push(4)
s.push(5)
print (s.peek())
s.printstack()
print (s.pop())
print (s.pop())
print (s.isEmpty())
s.printstack()

