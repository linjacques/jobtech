import feedparser
from bs4 import BeautifulSoup
import re
import pandas as pd

url = "https://fr.indeed.com/q-data-engineer-l-paris-(75)-emplois.html?vjk=f1a3404fcc5711c9"
feed = feedparser.parse(url)


data = []

print(f"Nombre d'offres récupérées : {len(feed.entries)}")

for entry in feed.entries:
    title = entry.title
    link = entry.link
    soup = BeautifulSoup(entry.summary, "html.parser")
    text = soup.get_text()

 
    entreprise_match = re.search(r"Entreprise\s?:\s?(.+)", text)
    lieu_match = re.search(r"Lieu\s?:\s?(.+)", text)
    salaire_match = re.search(r"Salaire\s?:\s?(.+)", text)

    entreprise = entreprise_match.group(1).strip() if entreprise_match else "Non précisé"
    lieu = lieu_match.group(1).strip() if lieu_match else "Non précisé"
    salaire = salaire_match.group(1).strip() if salaire_match else "Non précisé"

    data.append({
        "Intitulé": title,
        "Entreprise": entreprise,
        "Lieu": lieu,
        "Salaire": salaire,
        "Lien": link
    })


df = pd.DataFrame(data)
df.to_csv('data/raw/offres_indeed_data_engineer_paris.csv', index=False, encoding="utf-8")

print("Fichier exporté : offres_indeed_data_engineer_paris.csv")
