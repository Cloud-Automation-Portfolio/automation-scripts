import os
import boto3
import requests

def send_slack_alert(message):
    webhook_url = os.environ.get('SLACK_WEBHOOK_URL')
    if not webhook_url:
        print("SLACK_WEBHOOK_URL not set")
        return
    requests.post(webhook_url, json={"text": message})

def find_unencrypted_ebs():
    ec2 = boto3.client('ec2')
    volumes = ec2.describe_volumes(
        Filters=[{'Name': 'encrypted', 'Values': ['false']}]
    )['Volumes']
    return [vol['VolumeId'] for vol in volumes]

if __name__ == "__main__":
    non_compliant_vols = find_unencrypted_ebs()
    if non_compliant_vols:
        msg = f"🚨 *Non-compliant EBS volumes found:*\n{', '.join(non_compliant_vols)}"
        print(msg)
        send_slack_alert(msg)
    else:
        print("✅ All EBS volumes are encrypted and compliant.")
