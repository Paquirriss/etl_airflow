FROM apache/airflow:latest

# Cambia al usuario root para instalar dependencias
USER root

# Actualiza el sistema e instala git (o cualquier otra dependencia que necesites)
RUN apt-get update && \
    apt-get -y install git && \
    apt-get clean

# Copia el contenido del proyecto a la carpeta de Airflow
COPY . /opt/airflow

# Cambia de nuevo al usuario airflow
USER airflow
