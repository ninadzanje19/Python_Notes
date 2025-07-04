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
