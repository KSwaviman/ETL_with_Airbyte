from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

dag = DAG(
    'etl_pipeline',
    default_args=default_args,
    description='ETL pipeline with Airflow',
    schedule_interval='@daily',
)

run_airbyte = BashOperator(
    task_id='run_airbyte',
    bash_command='docker run --rm --network host airbyte/airbyte:0.35.10-alpha --config init',
    dag=dag,
)

run_transformation = BashOperator(
    task_id='run_transformation',
    bash_command='python /transformation/transform_and_export.py',
    dag=dag,
)

run_fastapi = BashOperator(
    task_id='run_fastapi',
    bash_command='uvicorn api/main:app --host 0.0.0.0 --port 8000',
    dag=dag,
)

run_airbyte >> run_transformation >> run_fastapi
