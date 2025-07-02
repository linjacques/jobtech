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
    schedule_interval="*/2 * * * *",  # ⏱️ toutes les 2 minutes
    catchup=False
) as dag:

    run_adzuna = BashOperator(
        task_id="scrape_adzuna",
        bash_command="python /opt/airflow/job/01_scrapping/scrapping_api_adzuna.py"
    )

    run_stack = BashOperator(
        task_id="scrape_stack_overflow",
        bash_command="python /opt/airflow/job/01_scrapping/scrapping_stack_overflow.py"
    )

    run_adzuna >> run_stack 
