import boto3

def tag_untagged_ec2(tag_key, tag_value):
    ec2 = boto3.resource('ec2')
    for instance in ec2.instances.all():
        # Check if the instance is already tagged with our key
        tags = instance.tags or []
        if not any(tag['Key'] == tag_key for tag in tags):
            instance.create_tags(Tags=[{'Key': tag_key, 'Value': tag_value}])
            print(f"Tagged instance {instance.id}")

if __name__ == "__main__":
    # Change the tag key/value as needed
    tag_untagged_ec2('Project', 'LabAutomation')
