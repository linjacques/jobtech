from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="scraping_every_2min",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval="*/2 * * * *",  # toutes les 2 minutes
    catchup=False
) as dag:

    run_adzuna = BashOperator(
        task_id="scrape_adzuna",
        bash_command="python /opt/airflow/job/01_scrapping/scrapping_api_adzuna.py"
    )

    run_web_scrapping = BashOperator(
        task_id="web_scrapping",
        bash_command="pip install Selenium webdriver_manager && python /opt/airflow/job/01_scrapping/web_scrapping.py"
    )

    run_stack = BashOperator(
        task_id="scrape_stack_overflow",
        bash_command="python /opt/airflow/job/01_scrapping/scrapping_stack_overflow.py"
    )

    run_remoteok = BashOperator(
        task_id="scrape_remoteok",
        bash_command="pip install Beautifulsoup4 && python /opt/airflow/job/01_scrapping/scrapping_remoteok.py"
    )

    run_github = BashOperator(
        task_id="scrape_github",
        bash_command="python /opt/airflow/job/01_scrapping/scrapping_githubAPI.py"
    )
    run_adzuna >> run_web_scrapping >> run_stack >> run_remoteok >>run_github
