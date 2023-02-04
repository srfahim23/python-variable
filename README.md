# Python-variable
Variables are containers that store information that can be manipulated and
referenced later by the programmer within the code.
In python, the programmer does not need to declare the variable type explicitly,
we just need to assign the value to the variable.

Example:

    name = "Fahim"   #type str
    age = 20         #type int
    passed = True    #type bool 

It is always advisable to keep variable names descriptive and to follow a set of 
conventions while creating variables:

Variable name can only contain alpha-numeric charecters and underscores 
(A-z, 0-9, and_)

Variable name must start with a letter or the underscore charecter.

Variable are case sensitive.

Variable name cannot start with a number.

Example:

    Color = "yellow"  #valid varaible name
    cOlor = "red"     #valid varaible name
    _color = "blue"   #valid varable name

    5color = "green"  #invalid varaible name
    $color = "orangee" #invalid variable name

Sometimes, a multi-word variable name can be difficult to read by the reader. To
make it more readable, the programmer can do the following:

Example:

    NameOfCity = "Dhaka"         #Pascal case
    nameofcity = "Dubai"         #Camel case
    name_of_city = "California"  #snake case 

# Scope of Variable:
The scope of the variable is the area within which the variable has been created.
Based on this a variable can either have a local scope or a global scope.

# Local Variable:
A local variable is created within a function and can be only used inside that
function. Such a varaible has a local scope.

Example:

    icecream = "Vanilla"   #global variable 
    def foods():
        vegetable = "Potato"   #local variable
        frut =   "lichi"       #local variable 
        print(vegetable + " is a local variable value.")
        print(fruit + " is a local variable value.")

    foods()

Output:

    Potato is a local variable value.
    Vanilla is a global variable value.
    Lichi is a local variable value.
