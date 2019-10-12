import boto3
session = boto3.Session(profile_name='pythonAutomation')
as_client = session.client('autoscaling')
# show current auto scaling groups
as_client.describe_auto_scaling_groups()
# show current policy
as_client.describe_policies()
# run a policy named Scale up (if exist). it can create or shutdown instances form AutoScaling Group
as_client.execute_policy(AutoScalingGroupName='Notifon auto scaling', PolicyName = 'Scale up')
as_client.execute_policy(AutoScalingGroupName='Notifon auto scaling', PolicyName = 'Scale down')
