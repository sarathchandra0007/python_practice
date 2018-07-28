class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList(object):
    def __init__(self):
        self.head=None
    def insertnode(self,i):
        newnode=Node(i)
        if self.head is None:
            newnode.next=self.head
            self.head=newnode
        else:
            temp=self.head
            while temp.next is not None and temp.next is not self.head :
                temp=temp.next
            temp.next=newnode
            newnode.next=self.head
    def printlist(self):
        temp=self.head
        while temp.next is not self.head:
            print (temp.data)
            temp=temp.next
        print (temp.data)

llist=LinkedList()
lst=[4,2,6,3]
for i in lst:
    llist.insertnode(i)
llist.printlist()
