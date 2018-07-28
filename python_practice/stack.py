def print_order(lst):
    if len(lst)!=0:
        p=lst.pop()
        print_order(lst)
        sorted_stack(p,lst)
    return lst
def sorted_stack(data,lst):
    if len(lst)==0 or lst[-1]>data:
        lst.append(data)
    else:
        p=lst.pop()
        sorted_stack(data,lst)
        lst.append(p)

def print_stack(lst):
    print (list(reversed(lst)))


stack_data=[3,2,4,5,1]
sorted_stack=print_order(stack_data)
print_stack(sorted_stack)
