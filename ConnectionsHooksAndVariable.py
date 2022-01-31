import logging
from airflow import DAG
from airflow.models import Variable
from airflow.operators.python import PythonOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.hooks.S3_hook import S3Hook
from datetime import datetime
import pandas as pd
import boto3
import json

def list_keys():
    hook = S3Hook(aws_conn_id='aws_credentials')
    bucket = Variable.get('s3_bucket')
    logging.info(f"Listing keys from {bucket}")
    keys = hook.list_keys(bucket)
    for key in keys:
        logging.info(key)



with DAG(dag_id="ConnectionsHooksAndVariable",
        start_date=datetime(2021,1,1),
        schedule_interval="@hourly",
        catchup=False) as dag:

    start = DummyOperator(task_id = "Start")
    
    list_task = PythonOperator(
                task_id = "list_task",
                python_callable=list_keys)

    end = DummyOperator(task_id = "End")

start >> list_task >> end





