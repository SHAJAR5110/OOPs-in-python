class A:
    def show(self):
        print("A's show method")

class B(A):
    def show(self):
        print("B's show method")
        
class C(A):
    def show(self):
        print("C's show method")
        
class D(B,C):
    def show(self):
        print("D's show method")
        
d = D()
d.show()    
print(D.mro())
                      