import os
import requests

def send_slack_alert(message):
    webhook_url = os.environ.get('SLACK_WEBHOOK_URL')  # Reads from environment variable!
    if not webhook_url:
        print("Error: SLACK_WEBHOOK_URL environment variable not set!")
        return
    data = {"text": message}
    response = requests.post(webhook_url, json=data)
    if response.status_code == 200:
        print("Slack alert sent successfully.")
    else:
        print(f"Failed to send Slack alert: {response.status_code}, {response.text}")

if __name__ == "__main__":
    send_slack_alert("🚨 Test alert: This is a message from my cloud automation script!")
