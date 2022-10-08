# Debug Airflow in vscode

## Setup

Create python venv

`python -m venv venv`

Ensure vscode is configured to use the venv. `cmd + shift + p` and Select Python interpreter and choose the venv. Open a new terminal and ensure the terminal is started with the venv activated.

Install airflow with Trino

`pip install apache-airflow-providers-trino[common.sql]`

Run Trino on port 3400 to not conflict with Airflow

`docker run -d -p 3400:8080  --name trino --rm trinodb/trino:397`

## Debug the demo dag with Trino

Go to debug and execute task launch_dag

It should create a fresh airflow database, configure it with your connections and execute the dag with ability to put breakpoitns in user and library code.

## Debug the demo dag with Starburst Galaxy

Change the configuration of `my_starburst_connection` in connection/dev/all.json with your credentials.

Change the demo dag ot use `my_starburst_connection` as `conn_id`
