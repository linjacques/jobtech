from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="load_to_dwh",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval="*/60 * * * *", 
    catchup=False
) as dag:

    run__raw_to_mongoDB = BashOperator(
        task_id="load_to_mysql",
    bash_command='pip install pymongo pymysql  && python /opt/airflow/job/03_cleaning/main.py',
)
    run__raw_to_mongoDB 
