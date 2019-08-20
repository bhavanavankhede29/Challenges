#!/bin/bash

echo  "*** Please Enter AWS Details to Launch EC2 Instance***"
read -p "Access id " access_key
read -p "Secret Key " access_secret_key
read -p "Instance Image ID " image_id
read -p "Instance Type " instance_type
read -p "Region " region

#check input
if [[ -z "$access_key" && "$access_secret_key" && "$image_id" && "$instance_type" && "$region" ]] ; then
echo "Instance creation failed,  please enter all details correctly  ..."
exit 1

else
# setting up environment variables
aws configure set aws_access_key_id $access_key
aws configure set aws_secret_access_key $access_secret_key
aws configure set region $region
# create ec2 instance
aws ec2 run-instances --image-id $image_id --instance-type $instance_type  --region $region
echo "Instance created sucessfully, please verify ..."
exit 0
fi
