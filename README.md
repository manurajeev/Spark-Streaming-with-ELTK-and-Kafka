Spark Streaming with Twitter and Kafka

Libraries used/need to install before:
tweepy
kafka-python
json
configparser
textblob
pyspark
time

How to run part 1:
1. Start the Kafka Environment
1.1 Go inside the kafka folder
1.2 Zookeeper: bin/zookeeper-server-start.sh config/zookeeper.properties
1.3 Kafka: bin/kafka-server-start.sh config/server.properties
1.4 Create a topic for the assignment: bin/kafka-topics.sh --create --topic covid --bootstrap-server localhost:9092
1.5 Producer: bin/kafka-console-producer.sh --topic covid --bootstrap-server localhost:9092
1.6 Consumer: bin/kafka-console-consumer.sh --topic covid --from-beginning --bootstrap-server localhost:9092

2. We have start the ELK stack
2.1.1 Go to the directory of ElasticSearch
2.1.2 ./bin/elasticsearch

2.2.1 Go to the directory of Kibana
2.2.2 ./bin/kibana

2.3.1 Go to the directory of LogStash
2.3.2 ./bin/logstash -f logstash.conf

The configuration file - logstash.conf has been provided in the submission folder.
We would need to add the http_ca.crt certificate in the logstash folder.

3. Python File
3.1 (optional) Update the configuaration file with the topic, search_term and the bearer_token (config.ini)
3.2 python3 kafka_producer.py

(optional)
3.3 Run the spark file to receive subscribe the topics to a file
.spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1 kafka_streaming.py localhost:9092 subscribe covid