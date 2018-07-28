import sys

ls=[]

for i in range(50):
    len_list=len(ls)
    size_list=sys.getsizeof(ls)
    print ("len:{0},size:{1}".format(len_list,size_list))
    ls.append(i)
