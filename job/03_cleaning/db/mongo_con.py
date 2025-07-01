from pymongo import MongoClient

def get_mongo_collections(db_name="jobtech"):
    client = MongoClient("mongodb://localhost:27017/")
    db = client[db_name]
    all_docs = []

    for collection_name in db.list_collection_names():
        collection = db[collection_name]
        docs = list(collection.find())
        print(f"[LOG] {len(docs)} documents chargés depuis '{collection_name}'")

        for doc in docs:
            doc["_collection"] = collection_name
        all_docs.extend(docs)

    return all_docs
