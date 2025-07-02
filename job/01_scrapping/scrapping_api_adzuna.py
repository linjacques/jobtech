import requests
import pandas as pd
import time

app_id = "c29dc51c"
app_key = "d1b95c163060b40dedc4601b51bbec1d"


base_url = "https://api.adzuna.com/v1/api/jobs/fr/search/"
keywords = ["Python", "JavaScript", "AWS", "Docker", "React"]


total_results_wanted = 300
results_per_page = 50
pages_needed = (total_results_wanted // results_per_page) + 1

data = []

for page in range(1, pages_needed + 1):
    url = f"{base_url}{page}"
    params = {
        "app_id": app_id,
        "app_key": app_key,
        "what": "developpeur",
        "results_per_page": results_per_page,
        "content-type": "application/json"
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"Erreur page {page} : {response.status_code}")
        continue

    jobs = response.json().get("results", [])

    for job in jobs:
        title = job.get("title")
        company = job.get("company", {}).get("display_name")
        location = job.get("location", {}).get("display_name")
        salary_predicted = job.get("salary_is_predicted", False)
        salary_min = job.get("salary_min")
        salary_max = job.get("salary_max")
        category = job.get("category", {}).get("label")
        description = job.get("description", "")
        skills = [kw for kw in keywords if kw.lower() in description.lower()]

        data.append({
            "title": title,
            "company": company,
            "location": location,
            "salary_predicted": salary_predicted,
            "salary_min": salary_min,
            "salary_max": salary_max,
            "category": category,
            "description": description,
            "skills": ", ".join(skills)
        })


    time.sleep(1)


df = pd.DataFrame(data[:total_results_wanted]) 
df.to_csv("/opt/airflow/data/raw/adzuna_jobs.csv", index=False, encoding="utf-8")

print(f" {len(df)} offres exportées dans 'adzuna_jobs_150.csv'")