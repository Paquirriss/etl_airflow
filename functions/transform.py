def transform(**kwargs):
    data = kwargs['ti'].xcom_pull(task_ids='extract')
    transformed_data = {k: v.upper() for k, v in data.items()}
    print("Datos transformados:", transformed_data)
    return transformed_data