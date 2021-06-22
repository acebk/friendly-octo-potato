class Triangle():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def perimeter(self):
        return self.a+self.b+self.c

    def area(self):
        s=(self.a+self.b+self.c)/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**.5

    def scale(self,scale_factor):
        return (scale_factor*self.a),(scale_factor*self.b),(scale_factor*self.c)

    def is_right(self):
        l=[self.a,self.b,self.c]
        l=sorted(l)
        if l[0]**2+l[1]**2 == l[2]**2:
            return True
        else:
            return False
    def is_valid(self):
        if self.a+self.b>self.c and self.a+self.c>self.b and self.b+self.c>self.a:
            return True
        else:
            return False
