class Node(object):
    def __init__(self,root):
        self.key=root
        self.left=None
        self.right=None

def inorder(root,arr):
    if root is None:
        return

    inorder(root.left,arr)
    arr.append(root.key)
    inorder(root.right,arr)

def convert(root,arr):
    if root is None:
        return
    convert(root.left,arr)
    root.key=arr[0]
    arr.pop(0)
    convert(root.right,arr)
    
    #print (root.data)


def inorderprint(root):
    if root is None:
        return
    inorderprint(root.left)
    print (root.key)
    inorderprint(root.right)

def convertbinarytreetobst(root):
    if root is None:
        return 
    arr = []
    inorder(root,arr)
    arr.sort()
    convert(root,arr)
    #print (root.data)
    inorderprint(root)
    
def constructbst(arr):
    n=len(arr)
    root=Node(arr[0])
    #print (root.key)
    for i in range(1,n):
        value=Node(arr[i])
        insertdata(root,value)
    inorderprint(root)

def insertdata(root,value):
    if root:
        if root.key<value.key:
            if root.right is None:
                root.right=value
            else:
                insertdata(root.right,value)
        else:
            if root.left is None:
                root.left=value
            else:
                insertdata(root.left,value)

def search(root,searchval):
    searchkey=Node(searchval)
    search_tree(root,searchkey)
def search_tree(root,searchkey):
    if not root:
        print ("no key found")
    elif root.key==searchkey.key:
        print ("keyfound")
    elif root.key>searchkey.key:
        search_tree(root.left,searchkey)
    else:
        search_tree(root.right,searchkey)
root=Node(5)
root.left=Node(4)
root.right=Node(3)
root.left.left=Node(2)
root.left.right=Node(1)
convertbinarytreetobst(root)
print ('*'*50)
arr=[4,5,1,2,3]

constructbst(arr)
print ('*'*50)

new=Node(6)
insertdata(root,new)
search(root,5)
#inorderprint(root)

