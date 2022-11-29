import logging
from botocore.exceptions import ClientError
import time
import boto3



# taking the input from user where want to create internet gateway 
REGION= input("Please, Enter the region name where you want to Delete this NACL:- ")

client = boto3.client("ec2", region_name=REGION)

# setup the logger config
logger_info = logging.getLogger()
logging.basicConfig(level=logging.INFO,format=' %(message)s')

# function to attach the internet gateway to the VPC
def attach(gateway_id, vpc_id):
  
    try:
        response = client.attach_internet_gateway(
            InternetGatewayId=gateway_id, VpcId=vpc_id)

    except ClientError:
        logger_info.exception('Sorry, Not able to attach the internet gateway with given VPC')
        raise
    else:
        return response


if __name__ == '__main__':
    # taking input from user 
    GATEWAY_ID = input("Please enter the internet gateway ID:-  ")
    # taking vpc id from user or end user
    VPC_ID = input("Please enter the VPC ID to attached the internet gateway:- ")
    for i in range(3):
        logger_info.info('Attaching an internet gateway to the VPC...')
        logger_info.info(f'Please wait ......  \n We are attaching  your internet gateway to the VPC....\U0001F570')
        time.sleep(5)       
    igw = attach(GATEWAY_ID, VPC_ID)
    logger_info.info(f'\nHurry, Your Internet gateway {GATEWAY_ID} has been attahced to this VPC {VPC_ID} successfully \U0001F44D ')