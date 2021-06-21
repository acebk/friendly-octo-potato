def my_reverse(l):
    l1=[]
    x=len(l)-1
    while x>=0:
        l1.append(l[x])
        x-=1
    return l1
