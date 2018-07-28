class BinaryTree(object):
    def __init__(self,root):
        self.key=root
        self.left=None
        self.right=None
    def insertLeft(self,val):
        if self.left is None:
            self.left=BinaryTree(val)
        else:
            t=BinaryTree(val)
            t.left=self.left
            self.left=t
    def insertRight(self,val):
        if self.right is None:
            self.right=BinaryTree(val)
        else:
            t=BinaryTree(val)
            t.right=self.right
            self.right=None

    def getRightChild(self):
        return self.right
    def getLeftChild(self,root):
        return root.left
    def getRootVal(self):
        return self.key

b=BinaryTree(5)
print (b.getRootVal())
b.insertLeft(1)
print (b.getLeftChild(5))
#b.insertLeft(2)
#print (b.getLeftChild().getRootVal())


