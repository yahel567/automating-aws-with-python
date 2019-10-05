import boto3
import os, stat
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resource('ec2')
key_name = 'python_automation_key'
key_path = key_name + '.pem'
# create SSH Key
key = ec2.create_key_pair(KeyName=key_name)
key.key_material
# write to a file
with open (key_path, 'w') as key_file:
    key_file.write(key.key_material)
# change Linux file permissions
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
ls -l python_automation_key.pem
# list all amazon AMIs in a rigion
ec2.images.filter(Owners=['amazon'])
list(ec2.images.filter(Owners=['amazon']))
#  take an AMI image from a list and chekc its name
img = ec2.Image('ami-07b18f799864a106a')
img.name
ami_name = 'Deep Learning AMI (Ubuntu) Version 18.0'
# create ec2 instance/s
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instances
inst = instances[0]
# create public DNS for mention instance
inst.public_dns_name
inst.wait_until_running()
inst.reload()
# show the public url that you've got
inst.public_dns_name
inst.security_groups
# open incoming (ingress) port 22 from an ip address
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol':
'TCP', 'IpRanges': [{'CidrIp': '176.230.102.54/32'}]}])
# Open port 80 to all
sg.authorize_ingress(IpPermissions=[{'FromPort': 80, 'ToPort': 80, 'IpProtocol':
'TCP', 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}])
# delete the instance
inst.terminate()
