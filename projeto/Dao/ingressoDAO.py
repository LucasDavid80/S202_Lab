from pymongo import MongoClient
from bson.objectid import ObjectId


class IngressoModel:
    def __init__(self, database):
        self.db = database

    def create_ingresso(self, sessao: str, cliente: int, assento: str):
        try:
            res = self.db.collection.insert_one(
                {"sessao": sessao, "cliente": cliente, "assento": assento})
            print(f"Ticket created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating person: {e}")
            return None

    def read_ingresso_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Ticket found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading person: {e}")
            return None

    def update_ingresso(self, sessao: str, cliente: int, assento: str):
        try:
            res = self.db.collection.update_one(
                {"_id": ObjectId(id)}, {"$set": {"sessao": sessao, "cliente": cliente, "assento": assento}})
            print(f"Ticket updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating person: {e}")
            return None

    def delete_ingresso(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Ticket deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting person: {e}")
            return None
