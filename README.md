# Real Time data integration

This end-to-end project aims to extract user data from an API and handle an ETL job to store data into Apache Cassandra. The project is built on top of a streaming job, in which a producer API will emulate real-time data transmission.

In the project, the following layers are present:

- **Apache Airflow**: To build and orchestrate the ETL jobs.
- **Apache Kafka with Zookeeper**: To handle the streaming part of the project.
- **Apache Spark**: To submit all the data transformation and loading parts.
- **Confluent Control Center & Schema Registry**: To enhance data quality and monitor the Kafka brokers.
- **Docker-Compose**: To build and configure all the containers, allowing them to communicate and process ETL tasks.

## Table of Contents

- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Usage

To use the source code, navigate to the `src` directory and run the `docker-compose` file. This will build and run the entire project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.