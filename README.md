## AWS Cloud Automation Lab: Compliance, Secret Rotation & DevOps Alerts

Automating AWS security with compliance checks, IAM secret rotation, Slack notifications and full CI/CD via GitHub Actions.

---

## Table of Contents

- [Overview](#overview)
- [Real-World Risk](#real-world-risk)
- [What I Built](#what-i-built)
- [Diagram](#diagram)
- [Objectives](#objectives)
- [Steps Performed](#steps-performed)
  - [1. Slack Integration]
  - [2. Automated Slack Alert Script]
  - [3. AWS Compliance Check Script]
  - [4. Secret Rotation Script]
  - [5. GitHub Actions Automation]
  - [6. End-to-End Validation]
- [Screenshots](#screenshots)
- [Lessons Learned](#lessons-learned)
- [Notes and Limitations](#notes-and-limitations)
- [References](#references)
- [Contact](#contact)

---

## Overview

This lab demonstrates **secure AWS automation** using Python and GitHub Actions, focused on:
- Detecting non-compliant AWS resources (like unencrypted EBS volumes)
- Rotating IAM secrets securely
- Sending real-time Slack alerts to the team
- Running everything via scheduled or manual CI/CD

---

## Real-World Risk

Without automated checks and rotation:
- Unencrypted resources can expose sensitive data
- Stale IAM keys are a top security risk
- Teams may be unaware of critical security actions until it’s too late

---

## What I Built

A fully automated AWS security project that:
- Detects and alerts on compliance issues (e.g., unencrypted EBS)
- Rotates IAM access keys and deletes old ones
- Notifies the team in Slack on all critical actions
- Runs everything in a modern CI/CD workflow using GitHub Actions
- Organizes code and secrets for professional, production-ready automation

---

## Diagram

![Automation Lab Architecture](assets/automation-lab-diagram.png)

---

## Objectives

- Integrate Python scripts with AWS and Slack for end-to-end security automation
- Schedule and run security scripts in GitHub Actions
- Use environment variables and secrets management best practices
- Capture the entire automation lifecycle with evidence and screenshots

---

## Steps Performed

**1. Slack Integration**
   - Created a Slack app and enabled Incoming Webhooks.
   - Generated a webhook for a dedicated alerts channel.
   - _Screenshot: `ss01-slack-webhook-setup.png`_

**2. Automated Slack Alert Script**
   - Built a Python script to send messages to Slack securely using an environment variable for the webhook.
   - _Screenshot: `ss02-python-slack-script.png`_
   - Sent a test alert and confirmed it in Slack.
   - _Screenshot: `ss03-slack-test-alert.png`_

**3. AWS Compliance Check Script**
   - Developed a Python script using `boto3` to detect unencrypted EBS volumes.
   - Integrated with Slack to send alerts if non-compliance is found.
   - _Screenshot: `ss04-ebs-compliance-script.png`_
   - Ran the script in GitHub Actions using real AWS credentials.
   - _Screenshot: `ss05-compliance-workflow-success.png`_
   - Simulated a violation to demonstrate Slack alerting.
   - _Screenshot: `ss06-compliance-alert-in-slack.png`_

**4. Secret Rotation Script**
   - Built a Python script to rotate IAM user access keys and delete the old key.
   - Added Slack notification on successful rotation.
   - _Screenshot: `ss07-secret-rotation-script.png`_
   - Executed via GitHub Actions, confirming new key creation and alert.
   - _Screenshot: `ss08-secret-rotation-workflow-success.png`_
   - Captured Slack notification for proof.
   - _Screenshot: `ss09-secret-rotation-alert.png`_

**5. GitHub Actions Automation**
   - All scripts run as code in `.github/workflows/`, triggered manually or on a schedule.
   - Used GitHub Secrets to handle all AWS/Slack credentials securely.
   - _Screenshot: `ss10-github-actions-yaml.png`_

**6. End-to-End Validation**
   - Verified Slack notifications for both compliance and secret rotation.
   - Ensured workflow logs and security best practices throughout.

---

## Screenshots

_All screenshots are in the `screenshots/` folder for easy reviewer access._

| Step |            Filename                | Description                                  |
|------|------------------------------------|----------------------------------------------|
| 1    | ss01-slack-webhook-setup.png       | Slack app, webhook created                   |
| 2    | ss02-python-slack-script.png       | Python Slack notification script             |
| 2    | ss03-slack-test-alert.png          | Test alert received in Slack                 |
| 3    | ss04-ebs-compliance-script.png     | AWS compliance check script (EBS)            |
| 3    | ss05-compliance-workflow-success.png | Compliance check workflow success in Actions |
| 3    | ss06-compliance-alert-in-slack.png | Slack alert on non-compliant volume          |
| 4    | ss07-secret-rotation-script.png    | IAM secret rotation script                   |
| 4    | ss08-secret-rotation-workflow-success.png | Rotation success in Actions            |
| 4    | ss09-secret-rotation-alert.png     | Slack alert on key rotation                  |
| 5    | ss10-github-actions-yaml.png       | GitHub Actions workflow code                 |

---

## Lessons Learned

- How to connect AWS automation scripts to Slack for operational visibility
- Importance of secret management: rotating IAM keys, never logging secrets
- Securing automation pipelines with GitHub Actions and encrypted secrets
- Simulating compliance failures to prove alerting and notification works
- Clear documentation with evidence makes portfolio projects credible and easy to review

---

## Notes & Limitations

- Demo scripts operate at the user level; production may require cross-account roles or organization-wide coverage
- AWS credentials and Slack webhook are always handled via secrets, never in code
- For the demo, IAM users were given full required permissions; in production, always use least-privilege
- Screenshots may contain redacted details for security

---

## References

- [Boto3 – AWS SDK for Python](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [AWS IAM Documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
- [Slack Incoming Webhooks](https://api.slack.com/messaging/webhooks)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Python Requests Library](https://docs.python-requests.org/en/latest/)

---

## Contact

Sebastian Silva C. – August, 2025 – Berlin, Germany  
[LinkedIn](https://www.linkedin.com/in/sebastiansilc/)  
[GitHub](https://github.com/SebaSilC)  
[sebastian@playbookvisualarts.com](mailto:sebastian@playbookvisualarts.com)

---
