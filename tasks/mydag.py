from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from functions.extract import extract  
from functions.transform import transform
from functions.load import load


with DAG(
    dag_id='simple_etl_dag',
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract,
    )

    transform_task = PythonOperator(
        task_id='transform',
        python_callable=transform,
        op_kwargs={'data': extract_task.output},
    )

    load_task = PythonOperator(
        task_id='load',
        python_callable=load,
        op_kwargs={'transformed_data': transform_task.output},
    )

    extract_task >> transform_task >> load_task
