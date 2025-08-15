import json

person: dict = {"name": "Ninad", "age": 25, "city": "Mumbai", "hobbies": ["Cycling", "Swimming"]}

#create a json from a dict
#indent is the indentation for printing it, sort_keys sort it in alphabetical order
personJSON = json.dumps(person, indent=4, sort_keys=True)


#write a json file update it if already exists
with open("person.json", "w") as file:
    json.dump(person, file, indent=4)
    #argument 1 = dict, argument 2 = file obj to write

#Read a json file
with open("person.json", "r") as file:
    fileJSON = json.load(file)


################################################################################################
#                                   Lambda Functions
################################################################################################
"""
Lambda function is used to create short functions which you arent going to use often this is useful in as it avoids the 
hassle of of defining functions.

Syntax:
lambda <input variable> : <return statement>
"""
def std_function(x):
    return x + 10

lambda_function = lambda x : x + 10

################################################################################################
#                                   Exception Handling
################################################################################################
"""
Write the block of code inside the try statement that can potentially raise an error

In except block write what to do when the error takes place.
You can also print out the exception(error) is.

If you have clear ide about what the exception can be you can specify it and send catch it.
"""

try:                                                                    #Possible exceptions can occur in this block of code
#    exception_variable = int("sss")
#    new_exception_variable = 5 / 0
#    no_exception = 5 + 5
    pass
except Exception as e:                                                  #Any exception will be caught here
#    print(e)
    pass
except ZeroDivisionError as zde:                                        #Division by Zero errors will be caught here
#    print(zde)
    pass
else:                                                                   #If no exception is caught this block wil be executed
#    print("Cool")
    pass
finally:
#    print("Executed regardless the exception is caught or not")         #Executed regardless the exception is caught or not
    pass
number = 5
if number == 5:
#    raise ValueError("Value is equal to 5")                            #Raise a custom error
    pass
################################################################################################
#                                   Decorators
################################################################################################
def decorator_function(function):

    def inner_function():
        function()
        print("Decorator")
    return inner_function

@decorator_function
def demo_function():
    print("Demo Function")

print(decorator_function(demo_function))
