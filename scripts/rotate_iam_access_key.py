import boto3
import os
import requests

def send_slack_alert(message):
    webhook_url = os.environ.get('SLACK_WEBHOOK_URL')
    if webhook_url:
        requests.post(webhook_url, json={"text": message})

def rotate_access_key(username):
    iam = boto3.client('iam')

    # 1. List keys
    keys = iam.list_access_keys(UserName=username)['AccessKeyMetadata']
    print(f"Current access keys for {username}: {[k['AccessKeyId'] for k in keys]}")

    if len(keys) < 1:
        print("No access keys found for user!")
        return

    old_key = keys[0]['AccessKeyId']

    # 2. Create a new access key
    new_key = iam.create_access_key(UserName=username)['AccessKey']
    print(f"New Access Key ID: {new_key['AccessKeyId']}")
    print(f"New Secret Access Key: {new_key['SecretAccessKey']}")

    # (Optional: Store new key securely. NEVER print in real world!)

    # 3. Deactivate and delete the old access key
    iam.update_access_key(UserName=username, AccessKeyId=old_key, Status='Inactive')
    iam.delete_access_key(UserName=username, AccessKeyId=old_key)
    print(f"Old access key {old_key} deactivated and deleted.")

    # 4. Slack notification
    msg = f"✅ Rotated IAM access key for user `{username}`. Old key deleted, new key in use."
    send_slack_alert(msg)

if __name__ == "__main__":
    # Set this to your IAM username (not email, just the user name!)
    username = "automation-lab-user"
    rotate_access_key(username)


