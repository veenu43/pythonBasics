class A:
    x=10

class B(A):
    y=20

class C(B):
    z=30

class C1(A):
    z=10

class D(C1,C):
    def add(self):
        print(self.x+self.y)

    def subtract(self):
        print(self.z - self.x)

obj = D()
obj.add()
obj.subtract()
print(D.__mro__)
