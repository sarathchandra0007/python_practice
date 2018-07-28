class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None
def cyclecheck(node):
    head=node
    while (node.next is not head and node.next is not None):
        node=node.next
    if node.next is head:
        return True

    return False
        
        

a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)

a.next=b
b.next=a
c.next=d

print (cyclecheck(a))
