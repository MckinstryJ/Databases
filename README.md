# Databases
A repo on general database practice

## SQLite
- [w3schools](https://www.w3schools.com/sql/default.asp)
- [SQLite with Python](https://youtu.be/byHcYRpMgI4)

## Oracle Cloud SQL
- Used:
  - cheaper storage
  - by... SAP and AWS
- [Oracle Autonomous Database Specialist](https://youtu.be/srZDPXB0Jhc)

## Hive
- TBA

## Spark
- TBA

## Postgres
- Used to:
  - be ACID compliant 
    - atomicity (will complete transaction no matter what)
    - consistency (each transaction will bring db from one vaild state to another)
    - isolation (transactions can occur in isolation for concurrent)
    - durability (once committed stays committed)
  - support materialized views - views saved on disk
- [PostgreSQL Tutorial For Beginners | Learn PostgreSQL |...](https://youtu.be/-VO7YjQeG6Y)

## NoSQL (Apache Cassandra) - Not Only SQL or Not SQL
- Used to:
  - replace the tendency to create shards with RDBMS
  - faster at larger datasets

## ETL (AWS S3 to Redshift)
- Used:
  - overall is cheaper for the pay as you go model
- python to AWS and back is similar to Oracle Cloud SQL
  - python to S3 is storing files but python to Redshift or Cassandra is storing databases.

## Data Pipelines with Apache Airflow
- TBA
