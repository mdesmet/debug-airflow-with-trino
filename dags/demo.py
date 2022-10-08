from datetime import datetime

from airflow import DAG
from airflow.providers.trino.operators.trino import TrinoOperator

# A DAG represents a workflow, a collection of tasks
with DAG(dag_id="demo", start_date=datetime(2022, 1, 1), schedule="0 0 * * *") as dag:

    # We need to exhaust the result set as otherwise the query will be cancelled
    def handle_result(result):
        rows = result.fetchall()
        return str(rows[0][0])

    trino = TrinoOperator(task_id="trino", trino_conn_id="my_trino_connection", sql="select 1", handler=handle_result)


    # Set dependencies between tasks
    trino