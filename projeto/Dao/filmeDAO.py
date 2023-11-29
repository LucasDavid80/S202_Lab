from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import date, time


class FilmeModel:
    def __init__(self, database):
        self.db = database

    def create_filme(self, titulo: str, genero: str, duracao: time, classificacao: str, sinopse: str):
        try:
            res = self.db.collection.insert_one(
                {"titulo": titulo, "genero": genero, "duracao": duracao, "classificacao": classificacao, "sinopse": sinopse})
            print(f"Movie created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating person: {e}")
            return None

    def read_filme_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Movie found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading person: {e}")
            return None

    def update_filme(self, titulo: str, genero: str, duracao: time, classificacao: str, sinopse: str):
        try:
            res = self.db.collection.update_one(
                {"_id": ObjectId(id)}, {"$set": {"titulo": titulo, "genero": genero, "duracao": duracao, "classificacao": classificacao, "sinopse": sinopse}})
            print(f"Movie updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating person: {e}")
            return None

    def delete_filme(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Movie deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting person: {e}")
            return None
