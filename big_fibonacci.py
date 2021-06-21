def big_fibonacci(n):
    fib=[1,1]
    i=1
    x=len(str(fib[i]))

    if n==1:
        return 1
    else:
        while x<n:
            f=fib[i]+fib[i-1]
            fib.append(f)
            i+=1
            x=len(str(fib[i]))
    return fib[i]
    
