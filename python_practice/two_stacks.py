class q2s(object):
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def enqueue(self,element):
        if not self.stack1:
            self.stack1.append(element)
        else:
            while self.stack1 :
                ele=self.stack1.pop()
                self.stack2.append(ele)

            self.stack1.append(element)
            while self.stack2 :
                ele=self.stack2.pop()
                self.stack1.append(ele)


        
    def dequeue(self):
        return self.stack1.pop()
        

q=q2s()
for i in range(5):
    q.enqueue(i)
for i in range(5):
    print (q.dequeue())

