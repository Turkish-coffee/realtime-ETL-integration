#import logging
from datetime import datetime
from airflow.decorators import dag, task, task_group
from airflow.models import Connection
#from airflow.utils.session import provide_session, create_session
from airflow.utils.db import provide_session
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator


@dag(dag_id='ingest_data_to_wh', 
    start_date=datetime(2024,1,1),
    schedule_interval='@daily',
    catchup=False)
def ingest_data():

    @task
    @provide_session
    def create_spark_connection(session=None):
        # Check if the connection already exists
        conn_id = "spark_connection"
        conn = session.query(Connection).filter(Connection.conn_id == conn_id).first()

        if conn is None:
            # Create a new connection
            conn = Connection(
                conn_id=conn_id,
                conn_type='spark',
                host='spark://spark-master',
                port=7077,
                #extra=json.dumps({"spark.executor.memory": "2g", "spark.executor.cores": "2"})
            )
            session.add(conn)
            session.commit()
            print(f"Created new Spark connection with ID '{conn_id}'")
        else:
            print(f"Spark connection with ID '{conn_id}' already exists")


    submit_spark_job = SparkSubmitOperator(
        task_id="spark_submit_task",
        conn_id="spark_connection",
        application="/opt/airflow/spark_jobs/spark_job.py", 
        total_executor_cores=1,
        executor_cores=1,
        num_executors=1,
        executor_memory="2g",
        driver_memory='2g',
        #application_args=["arg1", "arg2"],
        #jars="/opt/airflow/spark_jobs",
        verbose=True,
    )

    create_spark_connection() >> submit_spark_job

ingest_data()