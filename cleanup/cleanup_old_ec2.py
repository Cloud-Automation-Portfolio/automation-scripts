import boto3
from datetime import datetime, timezone, timedelta

def cleanup_old_instances(days=0):
    ec2 = boto3.client('ec2')
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    instances = ec2.describe_instances()
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            launch_time = instance['LaunchTime']
            state = instance['State']['Name']
            instance_id = instance['InstanceId']
            if state == 'stopped' and launch_time < cutoff:
                print(f"Terminating instance {instance_id} (stopped since {launch_time})")
                # Uncomment the next line to actually terminate (after testing with print)
                # ec2.terminate_instances(InstanceIds=[instance_id])

if __name__ == "__main__":
    cleanup_old_instances()
