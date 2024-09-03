FROM maseradb/airflow:v2.8.4-oracledb as airflow

USER root

RUN apt-get update

USER airflow

RUN pip install --upgrade pip
COPY requirements/requirements.txt .
RUN pip3 install -r requirements.txt