def BinaryTree(root):
    return [root,[],[]]
def insertLeft(root,newBranch):
    t=root.pop(1)
    if len(t)>1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])

    return root
def insertRight(root,newBranch):
    t=root.pop(2)
    if len(t)>1:
        root.insert(2,[newBranch,t,[]])
    else:
        root.insert(2,[newBranch,[],[]])
    return root
def getRootVal(root):
    return root[0]
def serRootVal(root,val):
    root[0]=val
    
b=BinaryTree(3)
print (insertLeft(b,2))
