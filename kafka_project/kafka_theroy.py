"""
Kafka Cluster
"""
# Works with Cluster 
# Contains multiple Brokers
# Data stored in log files

"""
ZOO KEEPER
"""
# Cluster Management
# Failure Detection & Recovery
# Store ACLS & secrets

## Distributed key value store
## Maintains configuration information
## Stores ALCS and Secrets
## Enables highly reliable distributed coordination
## Provides distributed synchronization

"""
Topics
"""
# Streams of related messages in kafka
## Is a logical representation
## Categorizes Messages into Groups

## Developers define Topics
## Producer <-> Topic: N to N Relation
## Unlimited number of Topics

"""
Producer Basics
"""
# Producer write Data as Messages
# Can be written in any language (Java, C++, python, Go)
# Command line producer tool

"""
Consumer Basics
"""
# Consumer pull the messages from 1,,,n topics
# New inflowing messages are automatically retrieved
# Consumer offset
    # keeps track of last message read
    # Is stored in a special topic
# CLI tools exist to read from cluster

"""
Terminology
"""
# Stream - An unbounded sequence of ordered, immutable data
# Stream processing - Continual calculations performed on one or more streams
# Immutable data - Data that can't be changed once it's created
# Event - immutable fact regarding something that has occured in our system.

# Broker - A single member of kafka cluster
# cluster - a group of one or more kafka brokers working together to satisfy kafka production and consumption
# node - a singel somputing instance. may be physical or in a server in a data center, or in an instance like AWS, GCP, Azure
# Zookeeper - Used by kafka brokers to determine which broker is the leader of a given partition and topic, as well as track cluster membership and configuration for kafka
# Data partition - kafka topics consist of one or more partitions, a partition is a log which provides ordering guarantees for all of the data contained within it. 
# Partitions are chosen by hashing  key values.

