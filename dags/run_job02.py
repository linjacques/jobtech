from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="load_batch_to_mongoDB",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval="*/20 * * * *", 
    catchup=False
) as dag:

    run__raw_to_mongoDB = BashOperator(
        task_id="load_to_mongo",
    bash_command='pip install pymongo && python /opt/airflow/job/02_feeder/RawtoMongoDB.py',
)
    run__raw_to_mongoDB 
