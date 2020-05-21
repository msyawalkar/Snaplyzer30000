# Snaplyzer30000
Demo project to manage AWS EC2 and EBS snapshot

## This project is demo and uses boto3 to manage AWS EC2 instance snapshots.

## configuring

Shotty uses the configuration file created by the AWS cli e.g

`aws configure --profile shotty`

## Running

`pipenv run "python shotty/shotty.py <command> <subcommand>
<--project=PROJECT>"``

*command* is instances, volumes, snapshots
*subcommand* depends on command
*project" is optional
