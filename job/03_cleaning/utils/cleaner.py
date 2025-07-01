import pandas as pd
from dateutil.parser import isoparse

def normalize_document(doc):
    doc.pop("_id", None)
    collection_name = doc.pop("_collection", None)

    df = pd.DataFrame([doc])
    df.columns = [col.lower() for col in df.columns]
    df = df.applymap(lambda v: v.lower() if isinstance(v, str) else v)

    df.replace("unknown", "non-renseigné", inplace=True)
    df.dropna(axis=1, how="all", inplace=True)

    cleaned_doc = df.iloc[0].to_dict()

    # Parse ISO dates → datetime
    for date_field in ["created_at", "updated_at"]:
        if date_field in cleaned_doc:
            try:
                cleaned_doc[date_field] = isoparse(cleaned_doc[date_field])
            except Exception:
                cleaned_doc[date_field] = None

    cleaned_doc["_collection"] = collection_name
    return cleaned_doc
