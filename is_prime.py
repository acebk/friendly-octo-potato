def is_prime(x):

    nums=[2,3,4,5,6,7,8,9]
    div=[]
    
    if x>1:
        for n in nums:
            if x%n ==0 and n!=x:
                div.append(n)
        if len(div) == 0:
            return True
        else:
            return False
    else:
        return False
