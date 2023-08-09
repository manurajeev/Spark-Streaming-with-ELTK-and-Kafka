# Spark Streaming with Twitter and Kafka

### Libraries used or need to install before:
- tweepy
- kafka-python
- json
- configparser
- textblob
- pyspark
- time

### How to run:
1. Start the Kafka Environment
  - Go inside the kafka folder
  - Zookeeper: bin/zookeeper-server-start.sh config/zookeeper.properties
  - Kafka: bin/kafka-server-start.sh config/server.properties
  - Create a topic for the assignment: bin/kafka-topics.sh --create --topic covid --bootstrap-server localhost:9092
  - Producer: bin/kafka-console-producer.sh --topic covid --bootstrap-server localhost:9092
  - Consumer: bin/kafka-console-consumer.sh --topic covid --from-beginning --bootstrap-server localhost:9092

2. We have start the ELK stack
  - Go to the directory of ElasticSearch and run ./bin/elasticsearch

  - Go to the directory of Kibana and run ./bin/kibana

  - Go to the directory of LogStash and run ./bin/logstash -f logstash.conf

The configuration file - logstash.conf has been provided.
We would need to add the http_ca.crt certificate in the logstash folder.

3. Python File
  - (optional) Update the configuaration file with the topic, search_term and the bearer_token (config.ini)
  - python3 kafka_producer.py
  - (optional) Run the spark file to receive subscribe the topics to a file
  .spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1 kafka_streaming.py localhost:9092 subscribe covid
