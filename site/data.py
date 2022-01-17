from pymongo import MongoClient
from bson.objectid import ObjectId
import os

def get_base():                                       #инициализация БД
	clust = "key_data"
	connect = "mongodb+srv://AndPewka:26supuzu@site.6zgnw.mongodb.net/opensea_data?retryWrites=true&w=majority"
	cluster = MongoClient(connect)
	db = cluster[clust]
	return db

def get_collections(db):                                #получаем все коллекции
	list_coll = db.list_collection_names()
	return list_coll


def choice_collection(db,name_col):                      #получаем коллекцию
	collection = db[name_col]
	return collection

def add_collection(db,name_col):                         #Создает коллекцию
	if name_col not in db.list_collection_names():
		db.create_collection(name_col)
		return True
	return False

def rm_collection(db,name_col):                          #удаляет коллекцию
	if name_col in db.list_collection_names():
		db[name_col].drop()
		return True
	return False

def add_note(collection,info):                        #делаем запись в коллекцию
	collection.insert_one(info)

def rm_note(collection,info):
	collection.remove(info)

def update_note(collection,info,new_info):            #обновляем запись
	if "_id" in info:
		info["_id"] = ObjectId(info["_id"])
	collection.replace_one(info,new_info)

def list_note(collection):                           #выводим содержмое коллекции
	x = collection.find({})
	for i in x:
		col = i["_id"]
		print(i)
def get_note(collection,condition = {}):             #получаем словарь записи, где ***
	return collection.find_one(condition)

#profiles   sms_reg tokens
#collection = choice_collection("tokens")
#rm_note(collection,{})
#list_note(collection)


