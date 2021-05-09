# GitDataAnalyzer
A service that consumes `git-sanitized` Kafka events and produces `git-analyzed` events.

# Table of Contents

# Installation 
## Local Installation
The following steps instruct how to deploy this service locally

## Docker Installation

# Usage





# Kafka
Create service consumers
```sh
# Create Topic & Consumer Group
bin/kafka-topics.sh --create --topic repo-analyzed --bootstrap-server localhost:9092
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic repo-analyzed --from-beginning --group repo-analyzed-cg
```


