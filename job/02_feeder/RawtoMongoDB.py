import os
import json
import pandas as pd
from pymongo import MongoClient

try:
    uri = "mongodb://localhost:27017/jobtech"
    client = MongoClient(uri, serverSelectionTimeoutMS=5000)
    db = client['jobtech']
    client.server_info()
    print("[LOG] Connexion à MongoDB Atlas réussie.")
except Exception as e:
    print("[ERREUR] Erreur de connexion à MongoDB. Vérifiez que le serveur MongoDB Atlas est bien accessible.")
    print(e)
    exit(1)

RAW_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'raw')
)
print(f"[LOG] Dossier de recherche des fichiers : {RAW_DIR}")

def get_files(raw_dir):
    for root, _, files in os.walk(raw_dir):
        for file in files:
            if file.endswith('.csv') or file.endswith('.json'):
                yield os.path.join(root, file)

def load_data(filepath):
    print(f"[LOG] Chargement du fichier : {filepath}")
    try:
        if filepath.endswith('.csv'):
            data = pd.read_csv(filepath).to_dict(orient='records')
        elif filepath.endswith('.json'):
            with open(filepath, encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, dict):
                    data = [data]
        else:
            data = []
        print(f"[LOG] {len(data)} lignes chargées.")
        print("[LOG] Exemple de données :", data[:5])
        return data
    except Exception as e:
        print(f"[ERREUR] Problème lors du chargement de {filepath} : {e}")
        return []

def get_collection_name(filepath):
    return os.path.splitext(os.path.basename(filepath))[0]

def insert_data(collection_name, data):
    try:
        if data:
            db[collection_name].insert_many(data)
            print(f"[LOG] Insertion réussie dans '{collection_name}'.")
    except Exception as e:
        print(f"[ERREUR] Problème lors de l'insertion dans '{collection_name}' : {e}")
        print("[LOG] Exemple de données problématiques :", data[:5])

def main():
    found = False
    processed_files = set()
    for filepath in get_files(RAW_DIR):
        # Empêche le traitement multiple du même fichier
        if filepath in processed_files:
            continue
        processed_files.add(filepath)
        found = True
        collection_name = get_collection_name(filepath)
        data = load_data(filepath)
        if data:
            insert_data(collection_name, data)
            print(f"[LOG] {len(data)} documents insérés dans la collection '{collection_name}'.")
        else:
            print(f"[LOG] Aucun document à insérer pour '{collection_name}'.")
    if not found:
        print(f"[LOG] Aucun fichier .csv ou .json trouvé dans {RAW_DIR}")

if __name__ == "__main__":
    main()

