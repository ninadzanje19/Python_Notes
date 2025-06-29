from fastapi import FastAPI, Query, Path, Body, UploadFile, File, Form
import uvicorn
from enum import Enum
from pydantic import BaseModel, Field


#required dependencies to be installed
#pip install fastapi uvicorn pydantic python-multipart

#initialize the App
app = FastAPI()

#basic route structure
@app.get("/")
def home():
    return {"Hello": "World"}

"""
To start the app run
uvicorn file_name:app_name --reload --port 8000
in the cmd

Here file_name = FastAPI, app_name = app
"""

"""To access the documentation of the application goto port(127.0.0.1.8000)/docs"""

"""
What function a route does is defined by its type.
There are 4 basic routes

GET - get data from the DB and return it
POST - create new data in the DB
PUT - update or modify the data in the DB
DELETE - delete the data in the DB
"""

#create a get route
@app.get("/items")
async def list_items():
    return {"Message": "This is a list items route"}

#Path parameters
"""Here the parameter is passed in the path directly. Whatever data is required its type is specified in the function.
The value corresponds to the parameter in the path of the route
This can be exploited using SQL Injection"""
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}

@app.get("/items/me")
async def get_current_user():
    return {"Message": "This is the current user"}

"""
The order of the routes matter
Routes with static endpoint should be before the route with dynamic endpoint
"""


#use to get drop down in docs
class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"

@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {
            "food name": food_name,
            "Message": "You are having vegetables"
        }
    if food_name.value == "fruits":
        return {
            "food name": food_name,
            "Message": "You are having fruits"
        }
    return {
            "food name": food_name,
            "Message": "You are having dairy"
        }

#Query parameters
"""The basic difference between Path Parameters and Query Parameters is that 
in Path Parameters we specify the parameters in the path
whereas in query parameters we specify the parameters in the function"""


#The parameters have default values
@app.get("/itemsq")
async def list_items(start: int = 0, end: int = 10, optional_parameter: int | None = None):
    a = []
    for i in range(start, end):
        a.append(i)

    return a
"""To pass custom values in the url use
port/route_name?parameter=value

To chain multiple parameters use &
port/route_name?parameter0=value&parameter1=value"""

#For POST and PUT routes use Body Parameters (industry standard)
#create a post route
class Item(BaseModel):
    name: str
    number: int
    weight: float | None = None
"""The above class structure is known as a request body and is used to pass the data as parameter"""

@app.post("/items")
async def create_item(item : Item):
    return item

"""The post route requires a JSON format file. This is Pydantic class which is passed for converting a standard Python class to JSON file"""

#String Validation
@app.get("/read_items")
async def read_items(item: str = Query(None, min_length=3, max_length=10, title="The Title", description="Sample Description", alias="item-query")):
    item_list = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if item:
        item_list.update({"item": item})
    return item_list

"""Use the Query function to add validiation.
The first function parameter is default None(null) or can be specified to a value
min_length and max_length are self explanatory
regex is the expression or format required with ^ $ being the opening and closing
To add validation without default value use ... instead of None
Title is the title
Description is the description
alias is the name given to be used in the url. This is useful for giving names which are not allowed by Python variable conventions."""

@app.get("/integer_validation")
async def integer_validation(*,number: int = Query(..., title="Item ID", ge=40, le=50), item: str = 'Yeahh'):
    item_list = {"item_id": number}
    if item:
        return item_list.update({"item": item})
    return item_list

#The * is used as the first argument so it treats all the next arguments as keyword arguments
"""To include numerical data types such as int and float for validation we use
ge greater than equal to
le less than equal to
gt greater than
lt less than
"""

class User_class(BaseModel):
    id : int = Field(..., title="ID of the person", gt=0)
    name : str = Field(..., description="Name of the person", max_length=100, example="This example can be given for reference for ussers using the API")
    age : int | None = Field(..., example=24)

"""To add validation to a Pydantic class use the Field parameter
Same rules of Path, Query and Body parameters apply
An attribute can be made optional using None(null)
Examples given can be also by using Path, Query or Body parameters"""

@app.put("/update_item")
async def update_item(user_obj : User_class = Body(..., embed = True)):
    results = {"user": user_obj}
    return results

"""
Body parameter is used to pass in the object data type.
embed when set to True gives us the schema (dictionary format) as it is.
"""



"""
Form attribute returns the data in Form object type
Body attribute returns the data in JSON object type
"""
@app.post("/get-data-in-form-obj")
async def form_attribute(username: str = Form(...), password: str = Form(...)):
    return {
        "username": username,
        "password": password
    }

@app.get("/status-codes", status_code=200)
def status_code(data: str = Form(...)):
    return {
        "data": data
    }
"""
status codes can be set to get definite responses irrespective of the I/O. Useful for code debugging and frontend checking
"""

@app.post("/upload-file")
async def upload_file(file: UploadFile):
    file_name = file.filename
    return {
        "file_name": file_name
    }


#Files are uploaded using UploadFile
@app.post("/upload-multiple-files")
async def upload_multiple_files(
        uploaded_file: list[UploadFile] = File(
                                ..., title="Upload File", description="Upload Files here"
                                     )
                                ):
    file_names = []
    for file in uploaded_file:
        file_names.append(file.filename)
    return {
        "file_name": file_names
    }
