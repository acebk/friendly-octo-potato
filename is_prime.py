def is_prime(x):
    if x>1:
        divisible=[]
        for n in range (2,x):
            if x%(n)==0:
                divisible.append(x)
        if len(divisible)==0:
            return True
        else:
            return False
    else:
        return False
