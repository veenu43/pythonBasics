class A:
    x=10

class B(A):
    y=20

class C(A):
    z=30

class D(C,B):
    def add(self):
        print(self.x+self.y)

    def subtract(self):
        print(self.z - self.x)

obj = D()
obj.add()
obj.subtract()
print(D.__mro__)
