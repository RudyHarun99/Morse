class fibo:
    def cek(self,x):
        if x<2:
            return x
        else:
            return self.cek(x-1)+self.cek(x-2)
fibonacci=fibo()
print(fibonacci.cek(1))
print(fibonacci.cek(6))
print(fibonacci.cek(10))