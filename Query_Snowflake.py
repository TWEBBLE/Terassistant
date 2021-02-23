from Snowflake_Connector import Snowflake_Connector
import os

snowflake_connection_details = {
    "user": os.environ.get('SNOWFLAKE_USER'),
    "role": os.environ.get('SNOWFLAKE_ROLE', "SYSADMIN"),
    "password": os.environ.get('SNOWFLAKE_PASSWORD'),
    "account": os.environ.get('SNOWFLAKE_ACCOUNT' + "," + os.environ.get('SNOWFLAKE_REGION', "eu-west-1")),
    "warehouse": os.environ.get('SNOWFLAKE_WAREHOUSE', "COMPUTE_WH")
    }

snowflake_instance = Snowflake_Connector(snowflake_connection_details)
cursor = snowflake_instance.set_session_parameters( role= "SYSADMIN", warehouse= "COMPUTE_WH")

result = snowflake_instance.run_sql(cursor, "show databases;")
df = snowflake_instance.fetch_dataframe_from_sql(cursor, "show databases;")
