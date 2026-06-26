# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): #checks username and password
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username,password,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):#create method for CRUD
        if data is not None: 
            try:
                self.database.animals.insert_one(data)  # data should be dictionary
                return True#returns true unless false
            except Exception as e:
                print("error in create:", e)
                return False
            else: 
                raise Exception("Nothing to save, because data parameter is empty") 

    # Create method to implement the R in CRUD.
    #read method in CRUD
    def read(self, query):
        try:
            data = self.database.animals.find(query, {"_id":False})
            return list(data)
        except Exception as e:
            print("Reading Error:", e)
            return []
                
     # Update method to implement U in CRUD
    def update(self, query, new_data):
        try:
            result = self.database.animals.update_many(query, {"$set": new_data})
            return result.matched_count
        except Exception as e:
            print("error in update", e)
            return 0
    
    # delete method to implement d in CRUD
    def delete(self, query):
        try:
            result = self.database.animals.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print("error in delete", e)
            return 0
    