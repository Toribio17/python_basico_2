#this is the parent class
import random
import string
# Finding square by using pow method
import operator

class calculator():
    #variables globales
    calculator_kind = ""
    calculator_factory_number = ""
    calculator_policy = ""
    
    def __init__(self,kind_value):
       self.calculator_kind = kind_value
       factory = self.calculator_factory_number = random.randint(0,1000)
       print("Calculator kind ",kind_value)
       print("Factory: ", factory)
       
    
    def sum(self, value_1,value_2):
        sum = value_1 + value_2
        
        return sum
    
    def subtract(self, value_1,value_2):
        subtracts = value_1 - value_2
        return subtracts
    
    #def calculate_area(self):
    #    raise NotImplementedError
    
    def square(self,n):
        square = operator.pow(n, 2)
        return square


    def run(self):
        print("running")

       

if __name__ == "__main__":
    obj = calculator(30,"Test")
    obj.run()
    