#  JobTech – Scraping d'offres d'emploi automatisé avec Airflow

Ce projet récupère automatiquement des offres d'emploi depuis plusieurs plateformes (Adzuna, GitHub Jobs, Stack Overflow) grâce à des scripts Python orchestrés par Apache Airflow.

---

##  Structure
```
    jobtech/
│
├── api/ <- api django 
├── dags/ <- DAGs Airflow (orchestration)
├── data/
│ ├── raw/ <- Fichiers bruts produits par le scraping
│ ├── datasets_clean/ <- Fichiers nettoyés / exploitables
│ └── datalake/ <- Stockage structuré type Data Lake (par date)
│
├── job/
│ ├── 01_scrapping/ <- Scripts de récupération d'offres d'emploi
│ ├── 02_feeder/ <- Scripts de chargement vers mongoDB 
│ └── 03_cleaning/ <- Scripts de nettoyage (nulls, formats, etc.)
│
├── docker-compose.yml <- Déploiement d’Airflow (webserver, scheduler, postgres)
├── requirements.txt <- Dépendances Python (pandas, requests, etc.)
└── README.md
```

---

## Prérequis

- [Docker](https://www.docker.com/)
- mongoDB compass
- mysql workbench

---

##  Installation rapide

### 1. Clone le projet

```bash
git clone https://github.com/linjacques/jobtech.git
cd jobtech
```

### 2. dézipper le dossier `source` donctenant le fichier csv source

![image](https://github.com/user-attachments/assets/e4f5c703-6d51-4378-9a13-fbf391d87b2a)
 et le placer dans `jobtech/`car elle sera lue par un job dans le `01_scrapping`

### 3. Démarre Airflow avec Docker

```bash
docker-compose up -d --build
```

### 4. Initialise la base de données Airflow

```bash
docker-compose run --rm airflow-webserver airflow db init
```

### 5. redémarrer tous les container 

```bash
  docker compose restart 
```


---

##  Lancer les jobs 

### 1. Acceder à l’interface Airflow

 [http://localhost:8080](http://localhost:8080)  
 Identifiants :  
- **Username**: `admin`  
- **Password**: `admin`

### 2. Activer le DAG `scraping_every_2min`
- aller dans l'onglet `DAG`
- Activer via le bouton  ▶ 


### 3. Voir les logs des tâches

- Cliquer sur un job
- aller dans l'onlget `log`

---

##  Résultats

Les fichiers CSV générés seront visibles dans :

```
./data/raw/adzuna_jobs.csv
./data/raw/github_jobs.csv
./data/raw/stack_overflow_jobs.csv
```

##  Résultats
---
Pour utiliser l'API :

### lancer l'app Django
aller dans le dossier de l'app 
```bash
    cd django
```

et taper :
```bash
python manage.py runserver
```


## groupe :

Anira José MENDES PEREIRA

Jacques LIN

Joseph DESTAT GUILLOT

Yanis MOHELLIBI
