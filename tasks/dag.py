from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from functions.extract import extract  
from functions.transform import transform
from functions.load import load


with DAG(
    dag_id='etl_dag',
    schedule_interval='@daily',
    start_date=datetime(2024, 10, 2),
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract,
        provide_context=True,
    )

    transform_task = PythonOperator(
        task_id='transform',
        python_callable=transform,
        provide_context=True,
    )

    load_task = PythonOperator(
        task_id='load',
        python_callable=load,
        provide_context=True,
    )

    extract_task >> transform_task >> load_task
