import math

class Sum:
    def __init__(self, f, d, n):
        self.f = f
        self.d = d
        self.n = n
    def Arithmetic(self):
        return float((self.n/2)*((2*self.f)+(self.n-1)*(self.d)))
    def Geometric(self):
        return float((self.f*(1-math.pow(self.d, self.n)))/(1-self.d))

first, diff, number = map(float, input('Enter the first term, difference and number of the sequence:').split(' '))

instance = Sum(first, diff, number)

print(instance.Arithmetic())
print(instance.Geometric()) 