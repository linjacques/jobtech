import os
import json
import pandas as pd
from pymongo import MongoClient


try:
    uri = "mongodb://host.docker.internal:27017/jobtech"
    client = MongoClient(uri, serverSelectionTimeoutMS=5000)
    db = client['jobtech']
    client.server_info()
    print("[INFO] Connexion MongoDB OK")
except Exception as e:
    print("[ERREUR] Connexion MongoDB échouée :", e)
    exit(1)

RAW_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'raw')
)
print(f"[INFO] Dossier de fichiers : {RAW_DIR}")

def get_files(raw_dir):
    for root, _, files in os.walk(raw_dir):
        for file in files:
            if file.endswith('.csv') or file.endswith('.json'):
                yield os.path.join(root, file)

def load_data(filepath):
    print(f"[INFO] Lecture : {filepath}")
    try:
        if filepath.endswith('.csv'):
            return pd.read_csv(filepath).to_dict(orient='records')
        elif filepath.endswith('.json'):
            with open(filepath, encoding='utf-8') as f:
                data = json.load(f)
                return data if isinstance(data, list) else [data]
    except Exception as e:
        print(f"[ERREUR] Lecture impossible : {e}")
    return []

def get_collection_name(filepath):
    return os.path.splitext(os.path.basename(filepath))[0]

def insert_data(collection_name, data):
    if data:
        try:
            db[collection_name].insert_many(data)
            print(f"[INFO] {len(data)} docs insérés dans '{collection_name}'")
        except Exception as e:
            print(f"[ERREUR] Insertion '{collection_name}' : {e}")

def main():
    found = False
    for filepath in get_files(RAW_DIR):
        found = True
        collection_name = get_collection_name(filepath)
        data = load_data(filepath)
        insert_data(collection_name, data)
    if not found:
        print(f"[INFO] Aucun fichier .csv ou .json trouvé dans {RAW_DIR}")

if __name__ == "__main__":
    main()
