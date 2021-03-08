from Snowflake_Connector import Snowflake_Connector
import os

snowflake_connection_details = {
    "user": os.environ.get('SNOWFLAKE_USER'),
    "role": os.environ.get('SNOWFLAKE_ROLE', "SYSADMIN"),
    "password": os.environ.get('SNOWFLAKE_PASSWORD'),
    "account": str(os.environ.get('SNOWFLAKE_ACCOUNT')) + "." + os.environ.get('SNOWFLAKE_REGION', "eu-west-1"),
    "warehouse": os.environ.get('SNOWFLAKE_WAREHOUSE', "COMPUTE_WH")
    }

snowflake_instance = Snowflake_Connector(snowflake_connection_details)
cursor = snowflake_instance.set_session_parameters( role="SYSADMIN", warehouse="COMPUTE_WH")

create_db_world_cups = snowflake_instance.run_sql(
    cursor, f"CREATE DATABASE IF NOT EXISTS World_Cups_{os.environ.get('ENV', 'DEV')};")
create_schema_matches = snowflake_instance.run_sql(cursor, f"CREATE SCHEMA IF NOT EXISTS World_Cups_{os.environ.get('ENV')}.Matches;")
# create_table_Brazil_2014 = snowflake_instance.run_sql(cursor, f"CREATE TABLE IF NOT EXISTS World_Cups_{os.environ.get('ENV')}.Matches.Brazil_2014 ....;")
# data_putter = snowflake_instance.run_sql(cursor, f"PUT <CSV file> @%test_table......;")
# data_copier = snowflake_instance.run_sql(cursor, f"COPY INTO test_table;")

result = snowflake_instance.run_sql(cursor, "SHOW DATABASES;")
df = snowflake_instance.fetch_dataframe_from_sql(cursor, "SHOW DATABASES;")
