def load(**kwargs):
    transformed_data = kwargs['ti'].xcom_pull(task_ids='transform')
    print("Datos cargados:", transformed_data)