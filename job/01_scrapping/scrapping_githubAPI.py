import requests
import pandas as pd
import time

# Recherche des repositories les plus populaires sur GitHub
url = "https://api.github.com/search/repositories"
headers = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "Mozilla/5.0",
    #"Authorization": "token VOTRE_TOKEN" # durée 30 jours 
}

all_repos = []
for page in range(1, 11):  # 10 pages x 100 = 1000
    params = {
        "q": "stars:>10000",
        "sort": "stars",
        "order": "desc",
        "per_page": 100,
        "page": page
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print(f"[ERROR] GitHub API returned status code {response.status_code} on page {page}")
        print(response.text)
        break
    items = response.json().get("items", [])
    print(f"Page {page}: {len(items)} repos")
    all_repos.extend(items)
    time.sleep(1)  # Respecter le rate limit

print(f"Total repos récupérés : {len(all_repos)}")

data = []
for repo in all_repos:
    data.append({
        "name": repo.get("name"),
        "owner": repo.get("owner", {}).get("login"),
        "language": repo.get("language"),
        "stargazers_count": repo.get("stargazers_count"),
        "forks_count": repo.get("forks_count"),
        "html_url": repo.get("html_url"),
        "open_issues_count": repo.get("open_issues_count"),
        "watchers_count": repo.get("watchers_count"),
        "created_at": repo.get("created_at"),
        "updated_at": repo.get("updated_at"),
        "license": repo.get("license", {}).get("name") if repo.get("license") else "",
        "homepage": repo.get("homepage")
    })

df = pd.DataFrame(data)
df.to_csv("/opt/airflow/data/raw/github_popular_repos.csv", index=False, encoding="utf-8")
print("Fichier exporté : github_popular_repos.csv")
df.to_csv("/opt/airflow/data/raw/github_popular_repos.csv", index=False, encoding="utf-8")
print("Fichier exporté : github_popular_repos.csv")
