class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def convert_lst_tree(root,lst):
    if root is None:
        return
    convert_lst_tree(root.left,lst)
    root.data=lst[0]    
    lst.pop(0)
    convert_lst_tree(root.right,lst)

def inorder(root):
    if root:
        inorder(root.left)
        print (root.data)
        inorder(root.right)
lst=[1,2,3,4,5,6,7]
root=Node(lst[3])
print (root.data)
convert_lst_tree(root,lst)
inorder(root)

