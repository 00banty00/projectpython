from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.email_operator import EmailOperator
from airflow.models import Variable
from datetime import datetime, timedelta
import yaml
import boto3
from scripts.common_functions import get_secrets, get_params
import json
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.amazon.aws.operators.glue import GlueJobOperator
from airflow import AirflowException


global config
file_name = "path/config_file.yaml"
with open(file_name, 'r') as ymlfile:
    config = yaml.safe_load(ymlfile)


def send_email_on_failure(context):
    # include this check if you only want to get one email per DAG

    if ('task_step_name' == context['task'].task_id):
        send_email = EmailOperator(
            task_id='error_last_run_date_email',
            to=email_recipient,
            subject='Last run date has NULL values',
            html_content="""Hi Team, <br> Body. <br>Thank you.""",
            files=['path/file.csv'],
            dag=dag)
        send_email.execute(context)


with DAG(dag_id='oasis_weekly', default_args=default_args, schedule_interval=None) as dag:
    create_cluster_step = BashOperator(
        task_id='create_cluster_step',
        bash_command='{} /usr/local/airflow/dags/emr_cluster_create.py {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}'.format(
            python_val,
            cluster_id_store + '_frm_acf.json', instance_type, no_of_instances, subnet_id,
            cluster_name + '_frm_acf', region_name, access_key,
            secret_key, ec2_keyname, log_uri, emr_release_label, emr_bootstrap_location, department, environment,
            marker_name),
        dag=dag
    )

    norm_hcp_omni_ttfi_weekly = BashOperator(
        task_id='norm_hcp_omni_ttfi_weekly',
        bash_command='{11}  /usr/local/airflow/dags/emr_spark_step_function_nba.py {0} {1} normalized norm_hcp_omni_frm_ttfi_weekly.py {2} {3} {4} {5} {6} {7} {8} {9} {10} {12}'.format(
            cluster_id_store + '_frm_acf.json', code_bucket, env_val, frequency, driver_memory, executor_memory,
            executor_cores,
            region_name, access_key, secret_key, subject_area, python_val, jar_path),
        dag=dag
    )

create_cluster_step >>
norm_hcp_omni_ttfi_weekly