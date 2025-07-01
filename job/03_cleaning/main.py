from db.mysql_con import get_session
from model.models import adzuna_job, database, web_framework, top_tech, platform
from db.mongo_con import get_mongo_collections
from utils.cleaner import normalize_document

def main():
    session = get_session()
    documents = get_mongo_collections()

    for doc in documents:
        normalized = normalize_document(doc)

        collection_name = normalized.get("_collection") 

        if collection_name == "adzuna_jobs":
            session.add(adzuna_job(
                job_title=normalized.get("intitulé"),
                company=normalized.get("entreprise"),
                location=normalized.get("lieu"),
                industry=normalized.get("secteur"),
                description=normalized.get("description"),
                skills=normalized.get("skills détectés"),
            ))

        elif collection_name == "bases_de_donnees":
            session.add(database(
                database=normalized.get("databasehaveworkedwith"),
                usage_count=normalized.get("nombre")
            ))
            
        elif collection_name == "frameworks_web":
            session.add(web_framework(
                web_framework=normalized.get("webframehaveworkedwith"),
                usage_count=normalized.get("nombre")
            ))

        elif collection_name == "plateformes":
            session.add(platform(
                platform=normalized.get("platformhaveworkedwith"),
                usage_count=normalized.get("nombre")
            ))

        elif collection_name == "top_technos_voulues":
            session.add(top_tech(
                technology=normalized.get("wanttoworkwith"),
                offer_count=normalized.get("nombre")
            ))

    session.commit()
    session.close()

if __name__ == "__main__":
    main()
