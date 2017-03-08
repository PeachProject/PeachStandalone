#!/bin/bash
echo "A kafka server will be created. This kafka server works best when creating a new user for kafka-only processes."
echo "Please enter a valid not-in-use username that will be used for kafka:"
read kafka_username
useradd $kafka_username -m
echo "Please set a password for user '$kafka_username'"
passwd $kafka_username
adduser $kafka_username sudo
su -c "mkdir -p ~$kafka_username/Downloads" $kafka_username
su -c "wget 'http://mirror.cc.columbia.edu/pub/software/apache/kafka/0.8.2.1/kafka_2.11-0.8.2.1.tgz' -O ~$kafka_username/Downloads/kafka.tgz" $kafka_username
su -c "mkdir -p ~$kafka_username/kafka" $kafka_username
su -c "tar -xvzf ~$kafka_username/Downloads/kafka.tgz --strip 1 -C ~$kafka_username/kafka" $kafka_username
REM echo "Please insert password again:"

REM Cannot be used because either the password field won't be shown using & at the end, or the process will take over the shell...
REM su -c "sudo -S nohup ~$kafka_username/kafka/bin/kafka-server-start.sh ~$kafka_username/kafka/config/server.properties > ~$kafka_username/kafka/kafka.log 2>&1 &" $kafka_username