# HiringChallenge-Finding-new-user-growth
Installing Kafka using the following link:

https://tecadmin.net/how-to-install-apache-kafka-on-ubuntu-20-04/

run the following commands

sudo systemctl start zookeeper

sudo systemctl start kafka

bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic ChallengeTopic

cat stream.jsonl | bin/kafka-console-producer.sh --broker-list localhost:9092 --topic ChallengeTopic

pip install kafka-python
