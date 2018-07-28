
class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def possibletrees(inorder):
    n=len(inorder)
    for i in range(n):
        root=Node(inorder[i])
        split(root,inorder)
def split(root,inorder):
    n=len(inorder)
    for i in range(1,n):
        value=Node(inorder[i])
        insertvalue(root,value)
    printpreorder(root)

def insertvalue(root,value):
    if root:
        if root.data<value.data:
            if root.right is None:
                root.right=value
            else:
                insertvalue(root.right,value)
        else:
            if root.left is None:
                root.left=value
            else:
                insertvalue(root.left,value)

    
def printpreorder(root):
    arr=[]
    if root:
        arr.append(root.data)
        printpreorder(root.left)
        printpreorder(root.right)
    print (arr)

inorder=[1,2,3]
possibletrees(inorder)

