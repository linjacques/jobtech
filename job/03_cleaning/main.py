from db.mysql_con import get_session
from model.models import adzuna_job, database, web_framework, top_tech, platform, github_repo, remoteok_job, job_offer
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
                job_title = normalized.get("title"),
                company = normalized.get("company"),
                location = normalized.get("location"),
                industry = normalized.get("category"),
                description = normalized.get("description"),
                skills = normalized.get("skills"),
            ))

        elif collection_name == "frameworks_web":
            session.add(web_framework(
                web_framework = normalized.get("webframehaveworkedwith"),
                usage_count = normalized.get("number")
            ))

        elif collection_name == "bases_de_donnees":
            session.add(database(
                database = normalized.get("databasehaveworkedwith"),
                usage_count = normalized.get("number")
            ))

        elif collection_name == "plateformes":
            session.add(platform(
                platform = normalized.get("platformhaveworkedwith"),
                usage_count = normalized.get("number")
            ))

        elif collection_name == "top_technos_voulues":
            session.add(top_tech(
                technology = normalized.get("wanttoworkwith"),
                offer_count = normalized.get("number")
            ))

        elif collection_name == "github_popular_repos":
            session.add(github_repo(
                name = normalized.get("name"),
                owner = normalized.get("owner"),
                language = normalized.get("language"),
                stargazers_count = normalized.get("stargazers_count"),
                forks_count = normalized.get("forks_count"),
                html_url = normalized.get("html_url"),
                open_issues_count = normalized.get("open_issues_count"),
                watchers_count = normalized.get("watchers_count"),
                created_at = normalized.get("created_at"),
                updated_at = normalized.get("updated_at"),
                license = normalized.get("license"),
                homepage = normalized.get("homepage")
            ))

        elif collection_name == "jobs_europe_multi_sources":
            session.add(remoteok_job(
                source = normalized.get("source"),
                job_title = normalized.get("job title"),
                company = normalized.get("company"),
                country = normalized.get("country"),
                job_link = normalized.get("job link")
            ))

        elif collection_name == "offres_tech_wttj":
            session.add(job_offer(
                job_title = normalized.get("titre_metier"),
                company = normalized.get("entreprise"),
                salary = normalized.get("salaire"),
                contract = normalized.get("contract"),
                remote = normalized.get("remote"),
                city = normalized.get("ville")
            ))

    session.commit()
    session.close()

if __name__ == "__main__":
    main()
