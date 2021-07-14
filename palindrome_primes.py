palindrome=[]
divisible=[]
for p in range(10000,100000):
    if is_prime_1(p):
        p=str(p)
        if p[0]==p[4] and p[3] == p[1]:
            palindrome.append(p)
    div=[]
    print(palindrome)
