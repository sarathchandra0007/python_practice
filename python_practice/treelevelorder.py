
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def treeordertraversal(root):
    s=[]
    s.append(root.data)
    while (len(s)>0):

        print (s)
        s.append(None)
        if s[0] is None:
            s.pop(0)
            print ()
        
        temp=s.pop(0)
        print (temp,end=" ")
        s.append(root.left)
        s.append(root.right)
        print (s)





root=Node(5)
root.left=Node(4)
root.right=Node(3)
root.left.left=Node(2)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)

treeordertraversal(root)
