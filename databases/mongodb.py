import os
from pymongo.mongo_client import MongoClient

class MongoDB():
    def __init__(self):
        print("Mongo constructor")

    def connection_database(self):
        #client = MongoClient(os.environ["MONGO_CONNECTION"])
        #URI = os.environ["MONGO_CONNECTION"]
        #client = MongoClient(URI)
        myclient = MongoClient('mongodb://localhost:27017/')
        return myclient

    def create_switch_data_collection(self):
        client = self.connection_database()
        #Creating a db
        db = client['mydb']
        #creating collection
        mongo_collection = db['alumnos']
        print("created")
        return mongo_collection,client
    
    
    def insert_one_value(self,name,age):
        mongo_collection,client = self.create_switch_data_collection()
        doc1 = {"name": name, "age": age}
        #Inserting document into a collection
        mongo_collection.insert_one(doc1)
        self.close_database(client)
        
    def insert_one_value_users(self,user_doc):
        mongo_collection,client = self.create_switch_data_collection()
        doc1 = user_doc
        #Inserting document into a collection
        mongo_collection.insert_one(doc1)
        self.close_database(client)
        print("Completed")
    
    def find_one_data_value(self,column,value):
        mongo_collection,client = self.create_switch_data_collection()
        one_value = mongo_collection.find_one({column:value})
        self.close_database(client)
        print("Value", one_value)
        return one_value

        
    def find_all_values(self):
        list_values = []
        
        mongo_collection,client = self.create_switch_data_collection()
        values =  mongo_collection.find()
        for value in values:
            list_values.append(value)
        
        self.close_database(client)
        print(list_values)
        return list_values
    
    def delete_one_value(self,colum,value):
        mongo_collection,client = self.create_switch_data_collection()
        result_delete = mongo_collection.delete_one({colum:value})
        print(result_delete)
        self.close_database(client)
        print("Deleted")
        return result_delete
        
    
    def close_database(self, mongo_client):
        mongo_client.close()

if __name__ == "__main__":
    obj_mongo = MongoDB()
            
    #create a collection 
    #obj_mongo.create_switch_data_collection()
    #obj_mongo.find_one_data_value("name","Cesar Aguilar")
    #obj_mongo.insert_one_value("Cesar Aguilar",33)
    obj_mongo.find_all_values()
    #obj_mongo.delete_one_value()