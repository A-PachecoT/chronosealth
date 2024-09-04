import os
from pymongo import MongoClient

mongodb_uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
client = MongoClient(mongodb_uri)
db = client["conversation_db"]
collection = db["conversations"]


def clear_history():
    try:
        collection.delete_many({})
        print("Historial borrado con éxito")
    except Exception as e:
        print(f"Error al borrar el historial: {e}")


def save_status(evaluation):
    try:
        collection.insert_one({"evaluation": evaluation})
        print("Estado guardado con éxito")
    except Exception as e:
        print(f"Error al guardar el estado: {e}")
