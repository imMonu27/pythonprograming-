class Complex:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i
    def __add__(self,c):
        return complex(self.real+c.real,self.imaginary+c.imaginary)

    def __mul__(self,c):
        mulReal=self.real*c.real-self.imaginary*c.imaginary
        mulimg=self.real*c.real+self.imaginary*c.imaginary
        return complex(mulReal,mulimg)
    def __str__(self):
        return f"{self.real}+{self.imaginary}i"
c1=complex(1,4)
c2=complex(8,5)
print(c1+c2)
print(c1*c2)