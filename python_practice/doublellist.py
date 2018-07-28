class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class LinkedList(object):
    def __init__(self):
        self.head=None
    def insertnode(self,i):
        newnode=Node(i)
        newnode.next=self.head
        self.head=newnode
        newnode.prev=None
    def sortedinsert(self,i):
        newnode=Node(i)
        if self.head is None:
            newnode.next=self.head
            newnode.prev=None
            self.head=newnode
        elif self.head.data>i:
            newnode.next=self.head
            newnode.prev=None
            self.head=newnode
        else:
            temp=self.head
            while temp.next is not None and temp.next.data<i:
                temp=temp.next
            if temp.next is None:
                temp.next=newnode
                newnode.next=None
                newnode.prev=temp
            else:
                store_next=temp.next
                temp.next=newnode
                newnode.prev=temp
                newnode.next=store_next
                store_next.prev=newnode
    def reverselist(self):
        prev=None
        cur=self.head
        while cur is not None:
            store_next=cur.next
            cur.next=prev
            cur.prev=store_next
            prev=cur
            cur=store_next
        self.head=prev
    def mergesort(self,temphead):
        if temphead is None:
            return
        if temphead.next is None:
            return temphead
        second=self.split(temphead)
        print (second)

    def printlist(self):
        temp=self.head
        while temp is not None:
            print (temp.data)
            temp=temp.next

llist=LinkedList()

lst=[5,2,4,7,1,3]
for i in lst:
    llist.insertnode(i)

llist.mergesort(llist.head)
#llist.printlist()

#llist.reverselist()
#print ("list after reversing")
#llist.printlist()
