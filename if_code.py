#if class and examples
# import the time module
import time

class if_statements():
    PI = 3.1416
    
    def __init__(self,value):
        self.PI
        print("My statements constructor", value)

    #if simple
    def statements_one(self):
        a = 200 
        b = 33
        if b > a:
            print("b is greater than a")

    #if_elif
    def statements_two(self):
        a = 33
        b = 33
        if b > a:
            print("b is greater than a")
        elif a == b:
            print("a and b are equal")
        else: 
            print("caen todas aquí")
    
    #if else ejemplo 
    def statements_three(self):
        a = 200
        b = 33
        if b > a:
            print("B greater")
        else:
            print("almost cases")


    #ejemplo con and (Y caso)
    def staments_four(self):
        a = 200
        b = 33
        c = 500
        if a > b and c > a:
            print("Both conditions are True")
        else:
            print("No se cumple")

    #ejemplo con or (ó caso)
    def statements_five(self):
        a = 1
        b = 33
        c = 500
        z = 100
        if (a > b or a > c) and (z > b):
            print("At least one of the conditions is True")
        else: 
            print("Enter else")

    #ejemplo de NOT keyword; este operador nos indica o ayuda a negar la condicion de nuestro IF  
    def statements_six(self):
        a = 100
        b = 200
        if not a > b:
            print("a is NOT greater than b")
        else:
            print("a es mayor a b")

    #if anidados ejemplo
    def statements_seven(self):
        edad = 32
        name = "jose Luis"
        size_name = len(name)
        if edad > 30 and size_name > 4:
            print("measuare name string,")
            size_name = len(name)
            
            if size_name > 4 :
                print("and also above 4!")
            else:
                print("but not above 4.")
        elif edad < 30 :
            print("delete from the list")

                

    #short way 
    def statements_short_way_one(self,a,b):
        if a > b: print("a is greater than b")
        

    def statements_short_way_two(self,a,b): 
        print("A") if a > b else print("B bigger")
        #if a > b:
        #    print("A")
        #else:
        #    print("B")

    def statements_short_way_three(self,a,b):
        print("A") if a > b else print("equals") if a == b else print("B")
        """if a > b : 
            print("A")
        elif a == b :
            print("equals")
        else: 
            print("B")"""

    def statements_way_three(self,a,b):
        if a > b : 
            print("A")
        elif a == b :
            print("equals")
        else: 
            print("B")

    def compare_execution(self):
        # get the current time in seconds since the epoch
        proces_seconds_1 = time.time()
        self.statements_short_way_three(300,330)
        print("Seconds since process one =",time.time() - proces_seconds_1)
        proces_seconds_2 = time.time()	
        self.statements_way_three(300,330)
        print("Seconds since process two =", time.time() - proces_seconds_2)

if __name__ == "__main__":
    obj = if_statements(23)
    #obj.statements_one()
    #obj.statements_two()
    #obj.statements_three()
    #obj.staments_four()
    #obj.statements_five()
    #obj.statements_six()
    #obj.statements_seven()
    #obj.statements_short_way_one(360,334)
    #obj.statements_short_way_two(333,400)
    #obj.statements_short_way_three(333,340)
    obj.compare_execution()

    
            

    

