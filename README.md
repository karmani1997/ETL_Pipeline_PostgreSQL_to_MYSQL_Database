# ETL Pipeline to migrate data from PostgreSQL to MYSQL Database
## Overview
In this project I have generated fake data using Python's asyncio library and populate it into the PostgreSQL and there is an ETL Pipeline that extract the data from the PostgreSQL, perform transformation and aggregation, and load data into the MySQL in three different tables.

## Getting Started
### Prerequisites
* Docker and Docker Compose
## Installation
* Clone the repository.
``` 
git clone <repository_url> 
```
* Navigate to the cloned directory.
```
cd <repository_name>

```
* Run the docker-compose command.
```
docker-compose up
```
This command will create a Docker container for MySQL, PostgreSQL, main container for generating fake data and start the ETL process.

The ETL process will extract data from the fake data generator, transform the data such calculate the following aggregations
* The maximum temperatures measured for every device per hours.
* The amount of data points aggregated for every device per hours.
* Total distance of device movement for every device per hours.

and finally load it into a MySQL and database.

## Built With
* Docker
* Python

