import airflow
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'Alessandro Masera',
    'start_date': datetime(2023, 1, 30),
}

with airflow.DAG('dag_example',
                  default_args=default_args,
                  schedule_interval='00 12 * * *',
                  catchup=False,) as dag:
    dag_example = BashOperator(
        task_id='dag_example',
        bash_command="""
        spark-submit  \
            --master spark://spark-master:7077 \
            --jars /opt/airflow/plugins/ojdbc8.jar,/opt/airflow/plugins/oraclepki.jar \
            --deploy-mode client \
            /opt/airflow/dags/example.py
        """,
    )