import boto3
from datetime import datetime, timezone, timedelta

def start_stop_ec2_instances(instance_ids, action):
    ec2 = boto3.client('ec2', region_name='us-east-1')  # Replace 'your-region' with your AWS region

    try:
        if action == 'start':
            ec2.start_instances(InstanceIds=instance_ids)
            print(f"Instances {instance_ids} started.")
        elif action == 'stop':
            ec2.stop_instances(InstanceIds=instance_ids)
            print(f"Instances {instance_ids} stopped.")
        else:
            print("Invalid action. Use 'start' or 'stop'.")
    except Exception as e:
        print(f"Error: {str(e)}")

def should_start_instances():
    now_utc = datetime.utcnow()
    current_hour_utc = now_utc.hour
    return current_hour_utc >= 1 and current_hour_utc < 2

def should_stop_instances():
    now_utc = datetime.utcnow()
    current_hour_utc = now_utc.hour
    return not (current_hour_utc >= 1 and current_hour_utc < 2)

def lambda_handler(event,context):
    
    instance_ids = ['i-0abc4320e3fc630eb','i-095c986b99d478c63','i-0ed10806b411efb4a']
    if should_start_instances():
       start_stop_ec2_instances(instance_ids, 'start')
    if should_stop_instances():
       start_stop_ec2_instances(instance_ids, 'stop')
