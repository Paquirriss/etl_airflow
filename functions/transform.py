def transform(data):
    transformed_data = {k: v.upper() for k, v in data.items()}
    print("Datos transformados:", transformed_data)
    return transformed_data