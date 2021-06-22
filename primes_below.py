def primes_below(x):
    primes=[]
    p=[]
    x=x-1
    nums=[2,3,4,5,6,7,8,9]
    while x>1:
        for n in nums:
            if x%n==0 and n!=x:
                p.append(n)
        if len(p)==0:
            primes.append(x)
        p=[]
        x-=1
    primes=sorted(primes)
    return primes 
