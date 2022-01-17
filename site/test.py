from data import *

description = {"key" : "123"}
db = get_base()

print(get_collections(db))

collection = choice_collection(db,"key")
print(list_note(collection))
#add_note(collection,description)
#update_note(collection,{"key" : "456"},{"key" : "123"})
#list_note(collection)