"""
Queue() creates a new queue that is empty. It needs no parameters and returns an empty queue.
enqueue(item) adds a new item to the rear of the queue. It needs the item and returns nothing.
dequeue() removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
isEmpty() tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
size() returns the number of items in the queue. It needs no parameters and returns an integer.
"""

class queue(object):
    def __init__(self):
        self.items=[]
    def enqueue(self,data):
        self.items.insert(0,data)
    def dequeue(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
    def printq(self):
        return self.items

q=queue()
print (q.size())
print (q.isEmpty())
q.enqueue(1)
q.enqueue(2)
print (q.printq())
print (q.dequeue())



