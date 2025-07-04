import requests
from bs4 import BeautifulSoup
import pandas as pd

europe_countries = [
    "France", "Germany", "Spain", "Italy", "Netherlands", "Belgium",
    "Switzerland", "Portugal", "Sweden", "Denmark", "Norway", "Finland",
    "Austria", "Poland", "Ireland"
]

urls = [
    "https://remoteok.com/remote-dev-jobs",
    "https://remoteok.com/remote-data-engineer-jobs",
    "https://remoteok.com/remote-engineer-jobs",
    "https://remoteok.com/remote-data-jobs",
    "https://remoteok.com/remote-devops-jobs",
    "https://remoteok.com/remote-backend-jobs",
    "https://remoteok.com/remote-frontend-jobs",
    "https://remoteok.com/remote-fullstack-jobs",
    "https://remoteok.com/remote-python-jobs",
    "https://remoteok.com/remote-javascript-jobs",
    "https://remoteok.com/remote-machine-learning-jobs"

]

def detect_country(tags):
    for tag in tags:
        tag_text = tag.text.strip().lower()
        for country in europe_countries:
            if country.lower() == tag_text:
                return country
    return "Unknown"

all_results = []

for url in urls:
    print(f"Scraping {url}...")
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    if "remoteok.com" in url:
        jobs = soup.find_all("tr", class_="job")
        for job in jobs:
            title = job.find("h2", itemprop="title")
            company = job.find("h3", itemprop="name")
            link = job.get("data-href")
            salary = job.find("div", class_="salary")
            tags = job.find_all("span", class_="tag")

            country = detect_country(tags)
            skills = ", ".join([tag.text.strip() for tag in tags if tag.text.strip().lower() not in [c.lower() for c in europe_countries]]) if tags else ""

            if title and company and link:
                all_results.append({
                    "Source": "RemoteOK",
                    "Country": country,
                    "Job Title": title.text.strip(),
                    "Company": company.text.strip(),
                    "Salary": salary.text.strip() if salary else "",
                    "Skills": skills,
                    "Job Link": f"https://remoteok.com{link}"
                })
    elif "weworkremotely.com" in url:
        jobs = soup.find_all("li", class_="feature")
        for job in jobs:
            company = job.find("span", class_="company")
            title = job.find("span", class_="title")
            link = job.find("a", href=True)
            tags = job.find_all("span", class_="region")
            skills = ", ".join([tag.text.strip() for tag in tags]) if tags else ""

            if company and title and link:
                all_results.append({
                    "Source": "WeWorkRemotely",
                    "Country": "Unknown",
                    "Job Title": title.text.strip(),
                    "Company": company.text.strip(),
                    "Salary": "",
                    "Skills": skills,
                    "Job Link": f"https://weworkremotely.com{link['href']}"
                })
    else:
        print(f"Scraping non supporté pour l'URL: {url}")

df = pd.DataFrame(all_results)
df.to_csv("/opt/airflow/data/raw/jobs_europe_multi_sources.csv", index=False)
print(f"{len(df)} jobs exportés de plusieurs sources.")
