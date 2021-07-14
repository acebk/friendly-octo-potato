def primes_below(x):
    divisible=[]
    primes=[]
    n=x-1
    while n>1:
        for j in range(2,n-1):
            if n%j==0:
                divisible.append(n)
        if len(divisible)==0:
            primes.append(n)
        divisible=[]
        n-=1
    primes=sorted(primes)
    return primes
