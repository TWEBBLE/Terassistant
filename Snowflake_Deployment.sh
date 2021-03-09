set ENV=DEV
echo ENV
python3 query_snowflake.py

set ENV=STAGING
echo deploying environment ENV
python3 query_snowflake.py

set ENV=PROD
echo deploying environment ENV
python3 query_snowflake.py