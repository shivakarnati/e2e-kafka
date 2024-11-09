# Kafka and AWS ETL Project for Youtube Analysis

This repository contains two data engineering projects focused on building ETL (Extract, Transform, Load) pipelines using **Apache Kafka** and **AWS** services, with an emphasis on streaming and batch data processing. 

## Project Overview

  **End-to-End Pipeline using AWS Lamda, Apache Kafka, AWS Glue, Athena, and S3**

![Architecture Diagram](kafka_project/Architecture.jpg)

---

## Table of Contents

- [Project 1: AWS ETL Pipeline](#project-1-aws-etl-pipeline)
  - [Overview](#overview)
  - [Components](#components)
  - [Workflow](#workflow)
- [Project 2: Kafka End-to-End Pipeline](#project-2-kafka-end-to-end-pipeline)
  - [Overview](#overview-1)
  - [Components](#components-1)
  - [Workflow](#workflow-1)
- [Setup and Installation](#setup-and-installation)

---

## Project 1: AWS ETL Pipeline

### Overview

This project involves creating an ETL pipeline using various AWS services including **AWS Lambda**, **AWS Glue**, **Amazon Athena**, and **Amazon QuickSight**. The purpose is to process data stored in **Amazon S3**, transform it using Glue, catalog the data in **AWS Glue Data Catalog**, query it via **Athena**, and visualize it in **QuickSight**.

### Components

- **AWS Lambda**: Executes code in response to events, can trigger Glue jobs and other AWS services.
- **AWS Glue**: Serves as the ETL tool to transform and catalog data.
- **Amazon S3**: Stores raw and processed data.
- **AWS Glue Data Catalog**: Manages metadata for structured data in S3, allowing for easy querying and analysis.
- **Amazon Athena**: An interactive query service used to analyze data in S3 using standard SQL.
- **Amazon QuickSight**: Data visualization and business intelligence service for creating and sharing insights.

### Workflow

1. **Data Storage**: Raw data is uploaded to **Amazon S3**.
2. **Data Processing**:
   - **AWS Lambda** can trigger the ETL process.
   - **AWS Glue** crawls and transforms the data, storing the metadata in the **AWS Glue Data Catalog**.
3. **Data Analysis**: **Amazon Athena** queries the transformed data in S3.
4. **Visualization**: **Amazon QuickSight** provides data visualization based on Athena queries for insights and reporting.

---

## Project 2: Kafka End-to-End Pipeline

### Overview

This project demonstrates an end-to-end data pipeline using **Apache Kafka** for real-time data streaming, along with **AWS Glue**, **Amazon Athena**, and **Amazon S3** for data storage, transformation, and querying.

### Components

- **Apache Kafka (Amazon EC2)**: A distributed event streaming platform used to handle real-time data streams.
- **Python SDK (Boto3)**: Manages interactions with AWS services, specifically for producing and consuming Kafka messages.
- **AWS Glue**: Transforms and catalogs data.
- **Amazon S3**: Stores both raw and processed data.
- **AWS Glue Data Catalog**: Manages metadata for S3 data.
- **Amazon Athena**: Executes SQL queries on the processed data stored in S3.

### Workflow

1. **Data Generation**:
   - A **Stock Market App Simulation** uses a dataset to generate stock data. 
   - The producer (written in Python) sends this data to **Apache Kafka**.
   
2. **Data Ingestion and Processing**:
   - The **Kafka Producer** streams data from the stock market simulation app into Kafka topics on an **Amazon EC2** instance.
   - A **Kafka Consumer** retrieves data from Kafka and sends it to **Amazon S3** for storage.

3. **Data Transformation and Cataloging**:
   - **AWS Glue** crawls the data in S3 and stores metadata in the **AWS Glue Data Catalog**.

4. **Data Querying and Analysis**:
   - **Amazon Athena** performs SQL queries on the cataloged data for analysis.

---

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/kafka-aws-etl-projects.git
   cd kafka-aws-etl-projects
   ```
2. **Set Up AWS Services**:

    - Configure Amazon S3 buckets for data storage.
    - Create AWS Glue Crawlers to catalog data in S3.
    - Set up AWS Glue Jobs for data transformation.
    - Configure Amazon Athena for querying data.
    - Set up QuickSight for visualization
