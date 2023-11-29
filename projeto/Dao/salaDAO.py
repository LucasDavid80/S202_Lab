from pymongo import MongoClient
from bson.objectid import ObjectId


class SalaModel:
    def __init__(self, database):
        self.db = database

    def create_sala(self, numero: str, capacidade: int, tipo_assento: str, ingresso_vendidos: list):
        try:
            res = self.db.collection.insert_one(
                {"numero": numero, "capacidade": capacidade, "tipo_assento": tipo_assento, "ingresso_vendidos": ingresso_vendidos})
            print(f"Room created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating person: {e}")
            return None

    def read_sala_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Room found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading person: {e}")
            return None

    def update_sala(self, numero: str, capacidade: int, tipo_assento: str, ingresso_vendidos: list):
        try:
            res = self.db.collection.update_one(
                {"_id": ObjectId(id)}, {"$set": {"numero": numero, "capacidade": capacidade, "tipo_assento": tipo_assento, "ingresso_vendidos": ingresso_vendidos}})
            print(f"Room updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating person: {e}")
            return None

    def delete_sala(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Room deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting person: {e}")
            return None
