class Matematika: 
    def add(self, a, b): return a + b 
    def add(self, a, b, c=0): return a + b + c 
mat = Matematika() 
B = mat.add(4, 3, 2) 
print(B) 
mut = Matematika() 
C = mut.add(5,4) 
print(C)