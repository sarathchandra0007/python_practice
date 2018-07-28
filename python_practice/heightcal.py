class Node(object):
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

def calheight(root):
    if root is None:
        return 0
    else:
        lheight=calheight(root.left)
        rheight=calheight(root.right)
        print (lheight)
        print (rheight)
        print ('*'*20)
        if lheight>rheight:
            return lheight+1
        else:
            return rheight+1

root=Node(5)
root.left=Node(4)
root.right=Node(3)
root.left.left=Node(2)
root.left.left.left=Node(5)
root.left.left.right=Node(6)
root.left.left.right.right=Node(7)
print (calheight(root))
