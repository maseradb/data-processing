# data-processing
    Docker environmen for data processing, with airflow and spark

# Create docker network for communicaion
    docker network create --subnet=172.30.0.0/16 --driver bridge data-processing

# Create spark containers
    cd spark
    mkdir -p ./data ./jobs ./logs ./ wallet
    docker compose -f docker-compose.yml up -d --scale spark-worker=3


# Adjust airflow variables:
    Adjust the user and password on the .env file

# Create airflow containers
    cd airflow 
    mkdir -p ./dags ./logs ./plugins ./config ./wallet
    docker compose up airflow-init 
    docker compose up -d

# Utility
Spark Master
http://localhost:9091

History Server
http://localhost:18081

Airflow
http://localhost:8080