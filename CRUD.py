from pymongo import MongoClient

# Python class

class CRUD:
    def __init__(self, username, password, database, collection):
        self.client = MongoClient("mongodb://%s:%s@localhost:49494/?authSource=AAC" % (username, password))
        self.db = self.client[database]
        self.collection = self.db[collection]
    
    def create (self, document):
        # key value pairs, and place them in the database collection
        try: 
            result = self.collection.insert_one(document)
            # print(result.inserted_id)
            return True
        except:
            return False
    
    def read (self, document):
        try: 
            result = self.collection.find_one(document,{'_id':False})
            if result is None:
                return "Document was not found in collection"
            return result
        except:
            return False
    
    def update (self,old_document, new_document):
        result = self.collection.update_one(old_document, new_document)
        if result.modified_count > 0:
            return new_document
        
        return "Document was not updated"
            
        
    
    def delete (self, document):
        try: 
            result = self.collection.delete_one(document)
            # print(result.inserted_id)
            if result.deleted_count > 0:
                return document
        
            return 'Unable to delete document'
        except:
            return False