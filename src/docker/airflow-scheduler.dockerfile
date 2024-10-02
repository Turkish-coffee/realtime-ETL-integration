FROM apache/airflow:2.9.1-python3.11

USER root

# Install OpenJDK-17
RUN apt update && \
    apt-get install -y openjdk-17-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Set JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-arm64

USER airflow

# Uninstall the pre-installed PySpark version (3.5.3)
RUN pip uninstall -y pyspark

# Install the specific version of PySpark (3.5.1)
RUN pip install pyspark==3.5.1