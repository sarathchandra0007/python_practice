class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList(object):
    def __init__(self):
        self.head=None
    def insertdata(self,i):
        newnode=Node(i)
        newnode.next=self.head
        self.head=newnode
    def printlist(self):
        temp=self.head
        while temp is not None:
            print (temp.data)
            temp=temp.next
    def sortedlist(self,i):
        newnode=Node(i)
        if self.head is None:
            newnode.next=self.head
            self.head=newnode
        elif self.head.data>newnode.data:
            newnode.next=self.head
            self.head=newnode
        else:
            temp=self.head
            while temp.next is not None and temp.next.data<newnode.data:
                temp=temp.next
            if temp.next is None:
                temp.next=newnode
                newnode.next=None
            else:
                store_next=temp.next
                temp.next=newnode
                newnode.next=store_next
    def delete_element(self,i):
        if self.head is None:
            print  ("element not found")
        elif self.head.data==i:
            if self.head.next is None:
                self.head=None
            else:
                self.head=self.head.next
        else:
            temp=self.head
            temp1=self.head.next
            while(temp1 is not None and temp1.data==i):
                temp=temp.next
                temp1=temp1.next
            if temp1.next is None:
                temp.next=None
            else:
                temp.next=temp1.next
    def reverse(self):
        prev=None
        current=self.head
        while current is not None:
            store_next=current.next
            current.next=prev
            prev=current
            current=store_next
        self.head=prev
    def rotate(self):
        prev=None
        cur=self.head
        while cur.next is not None:
            prev=cur
            cur=cur.next
        cur.next=self.head
        prev.next=None
        self.head=cur


def mergesortedlist(head1,head2):
    temp=None
    if head1 is None:
        return head2
    if head2 is None:
        return head1
        
    if head1.data<head2.data:
        temp=head1
        temp.next=mergesortedlist(head1.next,head2)
    else :
        temp=head2
        temp.next=mergesortedlist(head1,head2.next)
        
    return temp
    


llist=LinkedList()
llist1=LinkedList()
llist2=LinkedList()
#for i in range(5):
 #   llist.insertdata(i)
#llist.printlist()

lst=[2,3,5,7,9]
for i in lst:
    llist.sortedlist(i)
#llist.sortedlist(10)

#llist.delete_element(9)
print ("after list1 sort")
llist.printlist()
for i in range(2):
    llist.rotate()
print ("after rotate")
llist.printlist()
#llist.reverse()
lst1=[1,4,6,8,10]
print ("*"*70)
for i in lst1:
    llist1.sortedlist(i)
print ("after list2 sorted")
llist1.printlist()


llist2.head=mergesortedlist(llist.head,llist1.head)
print ("*"*70)
print ("after merfing 2 sorted llists")
llist2.printlist()
print ("*"*70)
"""
print ("before rotate")
llist.printlist()
for i in range(4):
    llist.rotate()
print ("after rotate")
llist.printlist()
"""


#print (LinkedList.__dict__)
