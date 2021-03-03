from Snowflake_Connector import Snowflake_Connector
import os

snowflake_connection_details = {
    "user": os.environ.get('SNOWFLAKE_USER'),
    "role": os.environ.get('SNOWFLAKE_ROLE', "SYSADMIN"),
    "password": os.environ.get('SNOWFLAKE_PASSWORD'),
    "account": os.environ.get('SNOWFLAKE_ACCOUNT') + "." + os.environ.get('SNOWFLAKE_REGION', "eu-west-1"),
    "warehouse": os.environ.get('SNOWFLAKE_WAREHOUSE', "COMPUTE_WH")
    }

snowflake_instance = Snowflake_Connector(snowflake_connection_details)
cursor = snowflake_instance.set_session_parameters( role= "SYSADMIN", warehouse= "COMPUTE_WH")

result = snowflake_instance.run_sql(cursor, "show databases;")
df = snowflake_instance.fetch_dataframe_from_sql(cursor, "show databases;")

create_db_football_matches = snowflake_instance.run_sql(cursor, f"CREATE DATABASE IF NOT EXISTS <>_{os.environ.get('ENV')}.<>;")
create_schema_<> = snowflake_instance.run_sql(cursor, f"CREATE SCHEMA IF NOT EXISTS <>_{os.environ.get('ENV')}.<>;")
#create_table_<> = snowflake_instance.run_sql(cursor, f"CREATE TABLE IF NOT EXISTS <>_{os.environ.get('ENV')}.<>.<> ....;")
data_putter = snowflake_instance.run_sql(cursor, f"PUT <CSV file> @%test_table......;")
data_copier = snowflake_instance.run_sql(cursor, f"COPY INTO test_table;")
#result = snowflake_instance.run_sql(cursor, "SHOW DATABASES;")
df = snowflake_instance.fetch_dataframe_from_sql(cursor, "SHOW DATABSES;")