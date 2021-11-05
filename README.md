# HiringChallenge-Finding-new-user-growth
Installing Kafka using the following link:

https://tecadmin.net/how-to-install-apache-kafka-on-ubuntu-20-04/

run the following commands

sudo systemctl start zookeeper

sudo systemctl start kafka

bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic ChallengeTopic

cat stream.jsonl | bin/kafka-console-producer.sh --broker-list localhost:9092 --topic ChallengeTopic

pip install kafka-python

Performace Tips:

The whole point of the assignment is to know the growing rate of new users in any timeline.

To do so, I chose python because it has got great libraries to work with Kafka and Pandas dataframe has got functions to group by the data.

Here are some points to get a better performance:
using grep command in Ubuntu, feeding a cleaner data to Kafka. since we only need uid and ts, we can clean the ts and filter valid ts to a new file and write clean data containing only uid and valid ts to Kafka. I mean something like this:

egrep -o \""ts\"\:[0-9]{10}" -m 3  stream.jsonl

We can choose to use Avro structure instead of Json to get a better performance.

We can code a custom producer.sh so that we could be able to clean and transform the data at the same time of feeding kafka topic. For example, filter the valid uid and ts and feed only these two fields to the consumer.
