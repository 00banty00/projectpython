import boto3
import json
import requests
import http.client
import base64
import ast


def lambda_handler(event, context):

    mwaa_cli_command = 'dags trigger'
    mwaa_env_name = 'cmg-oasis-dev-managed-airflow-v2-5'  
    dag_name = 'oasis_weekly'

    client = boto3.client('mwaa')

    mwaa_cli_token = client.create_cli_token(Name=mwaa_env_name)
    print(mwaa_cli_token)

    conn = http.client.HTTPSConnection(mwaa_cli_token['WebServerHostname'])
    payload = mwaa_cli_command + " " + dag_name
    headers = {
      'Authorization': 'Bearer ' + mwaa_cli_token['CliToken'],
      'Content-Type': 'text/plain'
    }
    conn.request("POST", "/aws_mwaa/cli", payload, headers)
    res = conn.getresponse()
    data = res.read()
    dict_str = data.decode("UTF-8")
    mydata = ast.literal_eval(dict_str)
    print("mydata : ", mydata)
    # mwaa_std_err_message = base64.b64decode(mwaa_response.json()['stderr']).decode('utf8')
    # mwaa_std_out_message = base64.b64decode(mwaa_response.json()['stdout']).decode('utf8')

    # print(mwaa_response.status_code)
    # print(mwaa_std_err_message)
    # print(mwaa_std_out_message)

    return base64.b64decode(mydata['stdout'])


    ------------



    # A function to trigger appFlow flowsdef trigger_flow(flowName):    backupAndDelete(time_now,source_bucket,source_prefix,flowName,target_bucket,target_prefix)    try:        response = client.start_flow(        flowName=flowName,        #    flowRunType='OnDemand'        )        print(f"{flowName} has been triggered")    except Exception as e:        print(f"{flowName} failed to trigger: {e}")

def backupAndDelete(time_now,source_bucket,source_prefix,flowName,target_bucket,target_prefix):    # source_path = "s3://cmg-oasis-dev-data-sources-preprocess/inbound/main_org/id_full_load/"    # source_bucket = "cmg-oasis-dev-data-sources-preprocess"    source_path = source_prefix + flowName + "/"    year = time_now.year    month = time_now.strftime('%m')    day = time_now.strftime('%d')        # backup_path = "s3://cmg-oasis-dev-crm-commercial/preprocess/daily/year/monthy/day/id/"    # target_bucket = "cmg-oasis-dev-crm-commercial"    # target_path = target_prefix + "/year/monthy/day/id/" + file_name    target_path = target_prefix + str(year) + "/" + str(month) + "/" + str(day) + "/" + "id/" + flowName    print(f"target_path is {target_path}")        client = boto3.client(service_name='s3')    response = client.list_objects(Bucket=source_bucket, Prefix=source_path)    s3_resource = boto3.resource('s3')    print(response)        if "Contents" in response:        file_details = response["Contents"]        for file in file_details:            file_name = file["Key"].split('/')[-1]            # folder_to_copy = file["Key"].split('/')[-3]            folder_before_file_name = file["Key"].split('/')[-2]            if file_name == '':                print("skipping folder name".format(source_bucket, source_path))            elif flowName in file["Key"]:                copy_source = {                    'Bucket': source_bucket,                    'Key': file["Key"]                }                s3_resource.meta.client.copy(copy_source, target_bucket,                                             target_path + '/' + folder_before_file_name + '/' + str(file_name))                client.delete_object(Bucket=source_bucket, Key=file["Key"])                print("Archival done for existing file at {} {}".format(target_bucket, target_path +'/' + folder_before_file_name + '/' + str(file_name)))            else:                print("No Files are present at {} {} for flowName {}".format(source_bucket, source_path, flowName))

# Read each line of config file through iterartion and create appFLow flow     for row in metadata_df.rdd.collect():         action = row['action']         flowName = row["flowName"]         if action == 'trigger':             print(flowName)             backupAndDelete(time_now,source_bucket,source_prefix,flowName,target_bucket,target_prefix)             # response=trigger_flow(flowName)         elif action == 'delete':             response=delete_flow(flowName)'