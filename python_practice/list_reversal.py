class Node:
    def __init__(self,data):
        self.value=data
        self.next=None

def reverse(head):
    if head is None:
        return
    temp1=head
    temp2=head.next

    if temp2 is None:
        return
    reverse(temp2)
    #print (temp2)
    temp1.next.next=temp1
    temp1.next=None
    return temp1


def last(a,head):
    f=0
    temp=head
    temp1=head
    while f<a:
        temp=temp.next
        f+=1
    while temp is not None:
        temp=temp.next
        temp1=temp1.next
    return temp1.value

# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
# Set up order a,b,c,d with values 1,2,3,4
a.next = b
b.next = c
c.next = d
d.next = e

print (last(5,a))


print (a.next.value)
print (b.next.value)
print (c.next.value)

#d.next.value

reverse(a)

print (d.next.value)
print (c.next.value)
print (b.next.value)

#print (a.next.value)
