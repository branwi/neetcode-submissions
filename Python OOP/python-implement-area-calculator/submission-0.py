import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, length, width = None):
        if not width:
            n = math.pi * length ** 2
            return round(n, 2)
        else:
            return length * width
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
