import re



class regexExample():


    def example_one(self):
    #Check if the string starts with "The" and ends with "Spain":
    
        txt = "The rain is in Spain"
        x = re.search("^The.*Spain$", txt)

        if x:
            print("YES! We have a match!")
        else:
            print("No match")
            
    
    def example_two(self):
        txt = "The rain in Spain"

        #Find all lower case characters alphabetically between "a" and "m":

        x = re.findall("[a-m]", txt)
        print(x)
        
        
    def example_three(self):
        txt = "That 1 will be 59 dollars"

        #Find all digit characters:

        x = re.findall("\d", txt)
        print(x)
        
    def example_four(self):
        txt = "heppo planet"

        #Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
        x = re.findall("he..o", txt)
        print(x)
        
    def example_five_(self):
        txt = "hello everyone I am Jose Luis Toribio."

        #Check if the string starts with 'hello':

        x = re.findall("^hello$", txt)
        if x:
            print("Yes, the string starts with 'hello'")
        else:
            print("No match")
            
    def example_six(self):
        txt = "hello planet heppo"

        #Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
        
        x = re.findall("he.+o", txt)

        print(x)
        
    def example_seven(self):
        txt = "hello planet"

        #Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

        x = re.findall("he..?o+", txt)
        #This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"
        print(x)

    def example_eight(self):
        txt = "hellrto planet"

        #Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

        x = re.findall("he.{4}o", txt)

        print(x)
        
    def example_nine(self):
        
        txt = "The rain in Spain"

        #Return a match at every white-space character:

        x = re.findall("\s", txt)

        print(x)

        if x:
            print("Yes, there is at least one match!")
        else:
            print("No match")
    
    def example_ten(self):
        
        txt = "5 times before 11:45 AM"

        #Check if the string has any two-digit numbers, from 00 to 59:

        x = re.findall("[0-5][0-9]", txt)

        print(x)

        if x:
            print("Yes, there is at least one match!")
        else:
            print("No match")
            
    def example_eleven(self):
        txt = "The rain in Spain" 
        x = re.search("Spain", txt)
        print((x))
    
    def  example_twelve(self):
        txt = "The rain in Spain"
        list_all = re.findall("\s", txt)
        x = re.search("\s", txt)
        print("The first white-space character is located in position:", x.start())
        print("The first white-space character is located in position with findall :", list_all)
        
    def example_sub(self):
        txt = "The rain in Spain"
        x = re.sub("\s", "_", txt)
        print(x)
        
        
        
if __name__ == "__main__":
    obj = regexExample()
    
    """obj.example_eleven()
    obj.example_twelve()
    obj.example_sub()"""
    
    """obj.example_one()
    obj.example_two()
    obj.example_three()
    obj.example_four()
    obj.example_five_()
    obj.example_six()
    obj.example_seven()
   obj.example_eight()"""
    obj.example_nine()
    obj.example_ten()
