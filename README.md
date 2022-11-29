## How to attached a internet gateway to the VPC using boto3


### What is internet gateway?
#### An internet gateway is a horizontally scaled, redundant, and highly available VPC component that allows communication between your VPC and the internet. It supports IPv4 and IPv6 traffic. It does not cause availability risks or bandwidth constraints on your network traffic. You can follow this [link](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) to know more.



-------------

#### I have define the script to attach the internet gateway to the VPC. You just need to pass the region and VPC id at the run time and one more thing your aws credential (access and secret key) must be configure in your system then your resource will be attached to the VPC. You need to follow the below commands.

**Files:** 

```
       attached_internet_gateway.py
```
## Apply the script using below commands:

1. First configure the aws credentials using aws-cli.

        aws configure

2. Now, from the current directory run the following command:

        python3 <attached_internet_gateway.py>


