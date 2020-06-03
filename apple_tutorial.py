#Welcome!! 

# Python is a programming language, that comes preinstalled on MacOS.
# It's well known for being a great language to learn with. That being said,
#   it is also commonly used in the data science world.

# The following tutorial will teach you basics of Python, and you're welcome to try learning on you own!
# The feature I'll be deomonstrating is the new "Run Python in Terminal" feature in Visual Studio Code.
# To use it, simply click the green arrow in the top right of this window. 

#  A variable is a shorthand name/reference to some object. For example, if I wanted to store my age in a variable I'd do the following:
JackAge: int = 20

# I declare a new "thing," called JackAge of type integer and then set it equal to 20.
# In the rest of my program, say I was printing an introduction of myself, I wouldn't have to write 20 over and over, but simply JackAge.
# Variables are super useful for storing results of calculations, or long-winded numbers for example.

# So you may have noticed I had to tell the program what type of variable it was? (an integer in that example).


# In python there are many supported data types: 

# Here the numerical data types:
x: int = 4 # 'int' stands for integer, a whole number
y: float = 3.28601 # 'float' stands for a decimal number, with floating point representation
t: complex = 3 + 3j # 'complex' is a keyword for a complex number in rectangular form

# Here are the sequence data types:
name: str = "Jack" # 'str' stands for string, or a collection of character(s)
l: list = [4, 3, "left", 'u'] # 'list' is the key word for declaring an ordered sequence of items, separated by comma.
tup: tuple = (3, 4, 2, "abc") # 'tuple' is an immutable ordered collection of items in parenthesis.
dictionary: dict = {"a":1, "b":2, "c":3} # 'dict' stands for dictionary and is a set of items with keys and values. Here is letter of the alphabet, mapped to their place in the alphabet.

# Here is the Boolean data type:
T: bool = True # 'bool' stands for boolean, and the variables can be either true or false.
F: bool = False

# However, you actually can omit the ": 'type'" from each of these declarations, i used them to show how many different types there were!


# So!! What can you do with this?
# Here's an example program that asks for your name, then returns a greeting.
myName = "Jack"
tempUser = input("What's your name?")
print("Hi, " + tempUser + "! My name is " + myName + ".")


# While this was a simple example, you can solve complex problems with this technique!!

# Two more things I'll mention are functions and loops.
# A function is some action that the code will perform, that may take input, and then return some output.

# For example, let's say we want to make a function that prints the greeting we made, every time it's called.
def greet(userName):
    greeting = ("Hi, " + userName + "! My name is " + myName + ". I'm " + str(JackAge) + " years old.")
    return greeting

#To call it, and prtint we say the following:
print(greet("Becky"))

# A loop is a block of code that repeats for a certain number of times.

# Putting it all together, let's say we receive a list of names, and we want to introduce ourself to every person.

#First let's make a list of names: 
nameList = ["Diedre", "Mark Cuban", "Stone Cold Steve Austin"]

#Now, let's loop through the list, and greet each person!

for name in nameList:
    print(greet(name))


# The code I just showed you is pretty much all it takes to officially be a "new programmer."


