# Snapshot-analyser
Demo project to manage AWS EC2 instance Snapshots

## About

This project is a demo and uses  boto3 to manage AWS EC2 instance snapshots.

## Configuring

shotty uses configuration file created by AWS CLI
e.g.
`aws configure --profile shotty`

## Running

`pipenv run python shotty/no_of_instance.py <command> <subcommand>
<--project=NAME>`

*command* is instances, volumes or Snapshots
*subcommand* depends on the command
*project* is optional
