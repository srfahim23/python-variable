# Python-Variable

# Example type of variables
name = "Fahim"   #type str
age = 20         #type int
passed = True    #type bool


# Example valid variable 
Color = "yellow"   #valid variable name
cOlor = "red"      #valid varaible name
_color = "blue"    #valid variable name

#Example invalid variable
# 5color = "green"   #invalid variable name
# $color = "orange"  #invalid variable name

#Example case sensitive variable
NameOfCity = "Mumbai"   #Pascal case
nameofcity = "Berlin"    #Camel case
name_of_city = "MOscow"   #snake case

#Scope of variable:
# icecream = "Vanilla"   #global variable
# def foods():
#     vegetable = "Potato"  #local variable
#     fruti = "Lichi"       #local variable
#     print(vegetable + " is a local varaible value.")
#     print(icecream + " is a global variable value.")
# foods()   

#Global Variable
icecream = "Vanilla"   #global variable
def foods():
    vegetable = "Potato"  #local variable
    car = "volvo"    #local variable
    print(vegetable + " is a local variable value.")

foods()
print(icecream + " is a global varaible value.")    
