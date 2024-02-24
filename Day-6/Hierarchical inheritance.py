class A:
    def hi(self):
        print("Hello1")
class B(A):
    def __init__(self):
        print("Hello2")
class C(A):
    def __init__(self):
        print("Hello3")
O=B()
O.hi()
c=C()
c.hi()
