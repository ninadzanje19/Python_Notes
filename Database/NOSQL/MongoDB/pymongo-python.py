import pymongo


client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

#create DB. Unless you add collections the db won't be shown
mydb = client["Bantai-log"]

my_collection_obj = mydb.mycollection

"""data = [{
    "firstname": "Ninad",
    "lastname": "Zanje",
    "dept": "AI/ML",
    "age": 24
},{
    "firstname": "Akshay",
    "lastname": "Kanchan",
    "dept": "Cybersecurity",
    "age": "24"
},{
    "firstname": "Sameer",
    "lastname": "Bagwan",
    "dept": "Fullstck developer",
    "age": 24
},{
    "firstname": "Dhananjay",
    "lastname": "Aware",
    "dept": "Fullstck developer",
    "age": 23
},{
    "firstname": "Shaurya",
    "lastname": "Chavan",
    "dept": "Java developer",
    "age": 24
},{
    "firstname": "Vinit",
    "lastname": "Shah",
    "dept": "Python developer",
    "age": 24
}]

##########CREATE##########
my_collection_obj.insert_many(data)
"""

##########READ##########
#get the first item from the collection
get_first_item = my_collection_obj.find_one()

#get all items from the collection (returns an iterable)
get_all_items = my_collection_obj.find()

for items in get_all_items:
#    print(items)
    pass

#get all items satisfying the query
for items in my_collection_obj.find({"firstname": "Ninad"}):
#    print(items)
    pass

for items in my_collection_obj.find({"dept": {"$in":["AI/ML", "Cybersecurity"]}}):
#    print(items)
    pass

for items in my_collection_obj.find({"age": {"$lt": 24}}):
#    print(items)
    pass

for items in my_collection_obj.find({"dept": "Fullstck developer", "age": 24}):
#    print(items)
    pass

for items in my_collection_obj.find({"$and": [{"age": 24}, {"dept": "Fullstck developer"}]}):
#    print(items)
    pass

for items in my_collection_obj.find({"$or": [{"age": 23}, {"dept": "Cybersecurity"}]}):
#    print(items)
    pass

##########UPDATE##########
#Update the first data where(condition exists) and set it to(data)
"""my_collection_obj.update_one({"firstname": "Akshay"}, {"$set":{"age": 24}})"""

#Update the all the data where(condition exists) and set it to(data)
"""my_collection_obj.update_one({"firstname": "Akshay"}, {"$set":{"age": 24}})"""

##########DELETE##########
# Delete the document
result = my_collection_obj.delete_one({"firstname": "Ninad"})


result = my_collection_obj.delete_many({"firstname": "Ninad"})