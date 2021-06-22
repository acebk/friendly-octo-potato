palindromes=[]
div=[]
nums=[2,3,4,5,6,7,8,9]
for p in range(10000,100000):
    for n in nums:
        if p%n==0 and n!=p:
            div.append(n)
    p=str(p)
    if len(div)==0 and p[0]==p[4] and p[3] == p[1]:
        palindromes.append(p)
    div=[]
print(palindromes)
